#!/usr/bin/env python3
"""
Build a mapping from node titles to split file paths.
Scans ALL H1 titles in each split file (not just the first one).

Usage:
    python build_split_map.py --doc help
    python build_split_map.py --doc sdk
    python build_split_map.py --doc ue
    python build_split_map.py --all
"""

import json
import os
import re
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent


def normalize_title(title: str) -> str:
    """Normalize title for matching."""
    # Remove markdown formatting
    title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', title)  # [text](url) -> text
    title = re.sub(r'\*\*([^*]+)\*\*', r'\1', title)  # **text** -> text
    title = re.sub(r'\*([^*]+)\*', r'\1', title)  # *text* -> text
    title = re.sub(r'`([^`]+)`', r'\1', title)  # `text` -> text
    # Normalize whitespace and case
    title = ' '.join(title.split()).lower()
    return title


def build_split_map(split_dir: Path) -> dict:
    """
    Recursively build a map of normalized titles to split paths.
    Extracts ALL H1 titles from each file, not just the first one.
    """
    title_map = {}
    
    for root, dirs, files in os.walk(split_dir):
        # Sort for consistent ordering
        dirs.sort()
        files.sort()
        
        for filename in files:
            if not filename.endswith('.md'):
                continue
            
            full_path = Path(root) / filename
            relative_path = full_path.relative_to(split_dir)
            rel_path_str = str(relative_path)
            
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find ALL H1 titles (lines starting with single #)
                h1_titles = re.findall(r'^# (.+)$', content, re.MULTILINE)
                
                for title in h1_titles:
                    norm_title = normalize_title(title)
                    if norm_title and norm_title not in title_map:
                        title_map[norm_title] = rel_path_str
                
            except Exception as e:
                print(f"Error reading {full_path}: {e}")
    
    return title_map


CONFIGS = {
    "help": {
        "split_dir": WORKSPACE / "help" / "split",
        "output": WORKSPACE / "indexes" / "wwise_help_zh_split_map.json"
    },
    "sdk": {
        "split_dir": WORKSPACE / "sdk" / "split", 
        "output": WORKSPACE / "indexes" / "wwise_sdk_zh_split_map.json"
    },
    "ue": {
        "split_dir": WORKSPACE / "ue" / "split",
        "output": WORKSPACE / "indexes" / "wwise_ue_zh_split_map.json"
    }
}


def build_for_doc(doc_id: str):
    """Build split map for a single document."""
    config = CONFIGS[doc_id]
    split_dir = config["split_dir"]
    output = config["output"]
    
    if not split_dir.exists():
        print(f"[{doc_id}] Split directory not found: {split_dir}")
        return
    
    print(f"[{doc_id}] Scanning {split_dir}...")
    title_map = build_split_map(split_dir)
    
    print(f"[{doc_id}] Found {len(title_map)} title -> path mappings")
    
    # Save
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(title_map, f, ensure_ascii=False, indent=2)
    
    print(f"[{doc_id}] Saved to {output}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Build split path mapping")
    parser.add_argument("--doc", choices=["help", "sdk", "ue"], help="Build for specific doc")
    parser.add_argument("--all", action="store_true", help="Build for all docs")
    
    args = parser.parse_args()
    
    if args.all:
        for doc_id in CONFIGS:
            build_for_doc(doc_id)
            print()
    elif args.doc:
        build_for_doc(args.doc)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
