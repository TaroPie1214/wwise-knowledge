#!/usr/bin/env python3
"""
Build PageIndex tree with summaries for Wwise documentation.
Uses Anthropic API (claude-haiku-4-5-20251001) for summary generation.
"""

import asyncio
import aiohttp
import json
import os
import sys
import time
import re
from pathlib import Path
from typing import Optional, List, Dict, Any

# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)

# Configuration
API_BASE = os.environ.get("ANTHROPIC_BASE_URL", "").rstrip("/")
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
MODEL = "claude-haiku-4-5-20251001"
MAX_CONCURRENT = 10
SUMMARY_TOKEN_THRESHOLD = 200  # Characters, not tokens

# Paths
WORKSPACE = Path(__file__).parent.parent


def extract_nodes_from_markdown(markdown_content: str) -> tuple:
    """Extract header nodes from markdown content."""
    header_pattern = r'^(#{1,6})\s+(.+)$'
    code_block_pattern = r'^```'
    node_list = []
    
    lines = markdown_content.split('\n')
    in_code_block = False
    
    for line_num, line in enumerate(lines, 1):
        stripped_line = line.strip()
        
        if re.match(code_block_pattern, stripped_line):
            in_code_block = not in_code_block
            continue
        
        if not stripped_line:
            continue
        
        if not in_code_block:
            match = re.match(header_pattern, stripped_line)
            if match:
                title = match.group(2).strip()
                level = len(match.group(1))
                node_list.append({
                    'title': title, 
                    'line_num': line_num,
                    'level': level
                })

    return node_list, lines


def extract_node_text_content(node_list: list, markdown_lines: list) -> list:
    """Extract text content for each node."""
    for i, node in enumerate(node_list):
        start_line = node['line_num'] - 1
        if i + 1 < len(node_list):
            end_line = node_list[i + 1]['line_num'] - 1
        else:
            end_line = len(markdown_lines)
        
        node['text'] = '\n'.join(markdown_lines[start_line:end_line]).strip()
    
    return node_list


def build_tree_from_nodes(node_list: list) -> list:
    """Build hierarchical tree from flat node list."""
    if not node_list:
        return []
    
    stack = []
    root_nodes = []
    node_counter = 1
    
    for node in node_list:
        current_level = node['level']
        
        tree_node = {
            'title': node['title'],
            'node_id': str(node_counter).zfill(4),
            'text': node['text'],
            'line_num': node['line_num'],
            'nodes': []
        }
        node_counter += 1
        
        while stack and stack[-1][1] >= current_level:
            stack.pop()
        
        if not stack:
            root_nodes.append(tree_node)
        else:
            parent_node, parent_level = stack[-1]
            parent_node['nodes'].append(tree_node)
        
        stack.append((tree_node, current_level))
    
    return root_nodes


def get_all_nodes_flat(nodes: list, result: list = None) -> list:
    """Flatten tree to list."""
    if result is None:
        result = []
    for node in nodes:
        result.append(node)
        if node.get('nodes'):
            get_all_nodes_flat(node['nodes'], result)
    return result


async def generate_summary(
    session: aiohttp.ClientSession, 
    text: str, 
    title: str,
    semaphore: asyncio.Semaphore
) -> str:
    """Generate summary for a node using LLM."""
    
    # If text is short, use it directly
    if len(text) < SUMMARY_TOKEN_THRESHOLD * 4:  # ~4 chars per token
        return text[:500]
    
    prompt = f"""You are summarizing a section from Wwise audio middleware documentation.
Generate a concise 1-2 sentence summary in the same language as the content.
Focus on the key technical information.

Section title: {title}

Section content:
{text[:6000]}

Summary (1-2 sentences):"""

    payload = {
        "model": MODEL,
        "max_tokens": 150,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01"
    }
    
    async with semaphore:
        try:
            async with session.post(
                f"{API_BASE}/v1/messages",
                json=payload,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=60)
            ) as resp:
                if resp.status != 200:
                    error = await resp.text()
                    print(f"API error for '{title[:30]}': {error[:100]}")
                    return text[:300]
                
                data = await resp.json()
                return data["content"][0]["text"].strip()
        except Exception as e:
            print(f"Error for '{title[:30]}': {e}")
            return text[:300]


async def process_nodes_with_summaries(
    nodes: list,
    session: aiohttp.ClientSession,
    semaphore: asyncio.Semaphore,
    progress: dict
) -> None:
    """Process all nodes and add summaries."""
    
    async def process_one(node: dict) -> None:
        text = node.get('text', '')
        title = node.get('title', '')
        
        summary = await generate_summary(session, text, title, semaphore)
        
        # Add summary based on whether node has children
        if node.get('nodes'):
            node['prefix_summary'] = summary
        else:
            node['summary'] = summary
        
        # Remove text to reduce output size (optional - keep for debugging)
        # del node['text']
        
        progress['done'] += 1
        if progress['done'] % 100 == 0:
            elapsed = time.time() - progress['start_time']
            rate = progress['done'] / elapsed if elapsed > 0 else 0
            eta = (progress['total'] - progress['done']) / rate if rate > 0 else 0
            print(f"  Progress: {progress['done']}/{progress['total']} "
                  f"({rate:.1f}/s, ETA: {eta/60:.1f}m)")
    
    tasks = [process_one(node) for node in nodes]
    await asyncio.gather(*tasks)


async def build_pageindex(
    md_path: str,
    output_path: str,
    checkpoint_path: Optional[str] = None
) -> dict:
    """Main function to build PageIndex with summaries."""
    
    print(f"Loading markdown from {md_path}...")
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Extracting nodes...")
    node_list, lines = extract_nodes_from_markdown(content)
    print(f"  Found {len(node_list)} header nodes")
    
    print("Extracting text content...")
    nodes_with_content = extract_node_text_content(node_list, lines)
    
    print("Building tree structure...")
    tree = build_tree_from_nodes(nodes_with_content)
    
    # Get all nodes flat for processing
    all_nodes = get_all_nodes_flat(tree)
    total = len(all_nodes)
    print(f"  Total nodes: {total}")
    
    # Load checkpoint if exists
    start_idx = 0
    if checkpoint_path and os.path.exists(checkpoint_path):
        with open(checkpoint_path, 'r') as f:
            checkpoint = json.load(f)
            start_idx = checkpoint.get('processed', 0)
            print(f"Resuming from checkpoint: {start_idx}/{total}")
    
    # Progress tracking
    progress = {
        'done': start_idx,
        'total': total,
        'start_time': time.time()
    }
    
    print(f"Generating summaries for {total - start_idx} nodes...")
    
    # Process with concurrency limit
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)
    connector = aiohttp.TCPConnector(limit=MAX_CONCURRENT * 2)
    
    async with aiohttp.ClientSession(connector=connector) as session:
        # Process in batches for checkpointing
        batch_size = 100
        nodes_to_process = all_nodes[start_idx:]
        
        for i in range(0, len(nodes_to_process), batch_size):
            batch = nodes_to_process[i:i + batch_size]
            await process_nodes_with_summaries(batch, session, semaphore, progress)
            
            # Save checkpoint
            if checkpoint_path:
                with open(checkpoint_path, 'w') as f:
                    json.dump({'processed': progress['done']}, f)
    
    # Build final structure
    doc_name = Path(md_path).stem
    result = {
        'doc_name': doc_name,
        'structure': tree
    }
    
    # Save output
    print(f"Saving to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    # Clean up checkpoint
    if checkpoint_path and os.path.exists(checkpoint_path):
        os.remove(checkpoint_path)
    
    elapsed = time.time() - progress['start_time']
    print(f"Done! Processed {total} nodes in {elapsed/60:.1f} minutes")
    
    return result


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Build PageIndex with summaries")
    parser.add_argument("--doc", required=True, choices=["help", "sdk", "ue"],
                        help="Document to process")
    parser.add_argument("--resume", action="store_true", 
                        help="Resume from checkpoint")
    
    args = parser.parse_args()
    
    configs = {
        "help": {
            "md": WORKSPACE / "help" / "wwise_help_zh.md",
            "output": WORKSPACE / "indexes" / "wwise_help_zh_pageindex.json",
            "checkpoint": WORKSPACE / ".help_checkpoint.json"
        },
        "sdk": {
            "md": WORKSPACE / "sdk" / "wwise_sdk_zh.md",
            "output": WORKSPACE / "indexes" / "wwise_sdk_zh_pageindex.json",
            "checkpoint": WORKSPACE / ".sdk_checkpoint.json"
        },
        "ue": {
            "md": WORKSPACE / "ue" / "wwise_ue_zh.md",
            "output": WORKSPACE / "indexes" / "wwise_ue_zh_pageindex.json",
            "checkpoint": WORKSPACE / ".ue_checkpoint.json"
        }
    }
    
    config = configs[args.doc]
    
    asyncio.run(build_pageindex(
        str(config["md"]),
        str(config["output"]),
        str(config["checkpoint"]) if args.resume else None
    ))


if __name__ == "__main__":
    main()
