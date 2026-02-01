#!/usr/bin/env python3
"""
Generate PageIndex summaries for Wwise documentation.
Uses Anthropic API (claude-haiku-4-5-20251001) to generate node summaries.
"""

import asyncio
import aiohttp
import json
import os
import sys
import time
from pathlib import Path
from typing import Optional

# Configuration
API_BASE = os.environ.get("ANTHROPIC_BASE_URL", "").rstrip("/")
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
MODEL = "claude-haiku-4-5-20251001"
MAX_CONCURRENT = 10  # Concurrent API calls
SUMMARY_TOKEN_THRESHOLD = 200  # If text < this, use text as summary

# Paths
WORKSPACE = Path(__file__).parent.parent
INDEXES_DIR = WORKSPACE / "indexes"


async def call_llm(session: aiohttp.ClientSession, text: str, title: str) -> str:
    """Generate summary for a node."""
    
    prompt = f"""You are summarizing a section from Wwise audio middleware documentation.
Generate a concise 1-2 sentence summary of this section in the same language as the content.

Section title: {title}

Section content:
{text[:8000]}

Summary:"""

    payload = {
        "model": MODEL,
        "max_tokens": 200,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01"
    }
    
    try:
        async with session.post(
            f"{API_BASE}/v1/messages",
            json=payload,
            headers=headers,
            timeout=aiohttp.ClientTimeout(total=60)
        ) as resp:
            if resp.status != 200:
                error = await resp.text()
                print(f"API error: {error}")
                return ""
            
            data = await resp.json()
            return data["content"][0]["text"].strip()
    except Exception as e:
        print(f"Error calling LLM: {e}")
        return ""


def load_structure(path: str) -> dict:
    """Load existing structure JSON."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_document(path: str) -> list:
    """Load markdown document as lines."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()


def get_all_nodes_flat(nodes: list, result: list = None) -> list:
    """Flatten tree structure to list."""
    if result is None:
        result = []
    for node in nodes:
        result.append(node)
        if 'nodes' in node:
            get_all_nodes_flat(node['nodes'], result)
    return result


def get_node_text(doc_lines: list, node: dict, all_nodes: list) -> str:
    """Extract text content for a node."""
    start_line = node.get('line_num', 1) - 1
    
    # Find next node's line number
    node_idx = next((i for i, n in enumerate(all_nodes) if n.get('node_id') == node.get('node_id')), -1)
    if node_idx >= 0 and node_idx + 1 < len(all_nodes):
        end_line = all_nodes[node_idx + 1].get('line_num', len(doc_lines)) - 1
    else:
        end_line = len(doc_lines)
    
    # Limit text length
    text = ''.join(doc_lines[start_line:min(end_line, start_line + 100)])
    return text[:8000]


def count_tokens_approx(text: str) -> int:
    """Approximate token count (rough estimate)."""
    return len(text) // 4


async def process_batch(
    session: aiohttp.ClientSession,
    nodes: list,
    doc_lines: list,
    all_nodes: list,
    progress: dict
) -> None:
    """Process a batch of nodes concurrently."""
    
    async def process_one(node: dict) -> None:
        node_id = node.get('node_id', '?')
        title = node.get('title', '')
        
        # Get node text
        text = get_node_text(doc_lines, node, all_nodes)
        
        # If text is short, use it directly
        if count_tokens_approx(text) < SUMMARY_TOKEN_THRESHOLD:
            summary = text[:500]
        else:
            summary = await call_llm(session, text, title)
        
        # Add summary to node
        if 'nodes' in node and node['nodes']:
            node['prefix_summary'] = summary
        else:
            node['summary'] = summary
        
        progress['done'] += 1
        if progress['done'] % 50 == 0:
            elapsed = time.time() - progress['start_time']
            rate = progress['done'] / elapsed if elapsed > 0 else 0
            eta = (progress['total'] - progress['done']) / rate if rate > 0 else 0
            print(f"  Progress: {progress['done']}/{progress['total']} ({rate:.1f}/s, ETA: {eta/60:.1f}m)")
    
    tasks = [process_one(node) for node in nodes]
    await asyncio.gather(*tasks)


async def generate_summaries(
    structure_path: str,
    doc_path: str,
    output_path: str,
    checkpoint_path: Optional[str] = None
) -> None:
    """Main function to generate summaries for all nodes."""
    
    print(f"Loading structure from {structure_path}...")
    structure = load_structure(structure_path)
    
    print(f"Loading document from {doc_path}...")
    doc_lines = load_document(doc_path)
    
    # Get all nodes
    root_nodes = structure.get('structure', [])
    all_nodes = get_all_nodes_flat(root_nodes)
    total = len(all_nodes)
    print(f"Total nodes: {total}")
    
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
    
    # Process in batches
    connector = aiohttp.TCPConnector(limit=MAX_CONCURRENT)
    async with aiohttp.ClientSession(connector=connector) as session:
        batch_size = MAX_CONCURRENT * 2
        
        for i in range(start_idx, total, batch_size):
            batch = all_nodes[i:i + batch_size]
            await process_batch(session, batch, doc_lines, all_nodes, progress)
            
            # Save checkpoint
            if checkpoint_path and (i + batch_size) % 100 == 0:
                with open(checkpoint_path, 'w') as f:
                    json.dump({'processed': progress['done']}, f)
    
    # Save output
    print(f"Saving to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(structure, f, ensure_ascii=False, indent=2)
    
    # Clean up checkpoint
    if checkpoint_path and os.path.exists(checkpoint_path):
        os.remove(checkpoint_path)
    
    elapsed = time.time() - progress['start_time']
    print(f"Done! Processed {total} nodes in {elapsed/60:.1f} minutes")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate PageIndex summaries")
    parser.add_argument("--doc", required=True, help="Document name (help, sdk, ue)")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    
    args = parser.parse_args()
    
    doc_configs = {
        "help": {
            "structure": INDEXES_DIR / "wwise_help_zh_structure.json",
            "doc": WORKSPACE / "help" / "wwise_help_zh.md",
            "output": INDEXES_DIR / "wwise_help_zh_pageindex.json",
            "checkpoint": WORKSPACE / ".help_checkpoint.json"
        },
        "sdk": {
            "structure": INDEXES_DIR / "wwise_sdk_structure.json",
            "doc": WORKSPACE / "sdk" / "wwise_sdk_zh.md",
            "output": INDEXES_DIR / "wwise_sdk_zh_pageindex.json",
            "checkpoint": WORKSPACE / ".sdk_checkpoint.json"
        },
        "ue": {
            "structure": INDEXES_DIR / "wwise_ue_structure.json",
            "doc": WORKSPACE / "ue" / "wwise_ue_zh.md",
            "output": INDEXES_DIR / "wwise_ue_zh_pageindex.json",
            "checkpoint": WORKSPACE / ".ue_checkpoint.json"
        }
    }
    
    if args.doc not in doc_configs:
        print(f"Unknown doc: {args.doc}. Choose from: {list(doc_configs.keys())}")
        sys.exit(1)
    
    config = doc_configs[args.doc]
    
    asyncio.run(generate_summaries(
        str(config["structure"]),
        str(config["doc"]),
        str(config["output"]),
        str(config["checkpoint"]) if args.resume else None
    ))
