#!/usr/bin/env python3
"""
Build a mapping from node titles to split file paths.
This avoids needing to rebuild the full PageIndex.
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


def extract_title_from_filename(filename: str) -> str:
    """Extract title from split filename."""
    # Remove number prefix and extension
    name = re.sub(r'^\d+-', '', filename)
    name = name.replace('.md', '')
    # Replace hyphens with spaces
    name = name.replace('-', ' ')
    return name.lower()


def build_split_map(split_dir: Path, relative_base: str = "") -> dict:
    """
    Recursively build a map of normalized titles to split paths.
    """
    title_map = {}
    
    for item in sorted(split_dir.iterdir()):
        if item.is_dir():
            # Recurse into subdirectory
            sub_relative = f"{relative_base}/{item.name}" if relative_base else item.name
            sub_map = build_split_map(item, sub_relative)
            title_map.update(sub_map)
        elif item.suffix == '.md':
            # Extract title from file
            relative_path = f"{relative_base}/{item.name}" if relative_base else item.name
            
            # Read first few lines to get actual title
            try:
                with open(item, 'r', encoding='utf-8') as f:
                    lines = [f.readline() for _ in range(5)]
                    for line in lines:
                        line = line.strip()
                        if line.startswith('#'):
                            # Found title
                            title = re.sub(r'^#+\s*', '', line)
                            norm_title = normalize_title(title)
                            title_map[norm_title] = relative_path
                            break
            except Exception as e:
                print(f"Error reading {item}: {e}")
            
            # Also add filename-based title as fallback
            filename_title = extract_title_from_filename(item.name)
            if filename_title not in title_map:
                title_map[filename_title] = relative_path
    
    return title_map


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Build split path mapping")
    parser.add_argument("--doc", required=True, choices=["help", "sdk", "ue"])
    
    args = parser.parse_args()
    
    configs = {
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
    
    config = configs[args.doc]
    split_dir = config["split_dir"]
    output = config["output"]
    
    if not split_dir.exists():
        print(f"Split directory not found: {split_dir}")
        return
    
    print(f"Building split map from {split_dir}...")
    title_map = build_split_map(split_dir)
    
    print(f"Found {len(title_map)} title -> path mappings")
    
    # Save
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(title_map, f, ensure_ascii=False, indent=2)
    
    print(f"Saved to {output}")


if __name__ == "__main__":
    main()
