#!/usr/bin/env python3
"""
uniblock.py

Generates an Unciv-style JSON bulk block for a Unicode range.
Usage: python uniblock.py <block_name_or_hex>
"""

import unicodedata
import sys
from pathlib import Path
import urllib.request

# ==================== CONFIG ====================
WRAP = 38
CATEGORY = "⚑ FancyText Unicode ⚑"
OUTPUT_DIR = Path(".")
# ===============================================

# Load Unicode blocks
url = 'https://www.unicode.org/Public/16.0.0/ucd/Blocks.txt'
UNICODE_BLOCKS = []

for line in urllib.request.urlopen(url):
    line = line.decode('utf-8').strip()
    if not line or line.startswith('#'):
        continue
    range_part, name = line.split(';')
    start, end = range_part.split('..')
    UNICODE_BLOCKS.append((int(start, 16), int(end, 16), name.strip()))

def parse_hex(value):
    if isinstance(value, int):
        return value
    return int(str(value).strip().replace("0x", "").replace("U+", ""), 16)

def to_proper_case(name):
    """Convert ALL CAPS UNICODE NAME to Proper Case."""
    words = name.lower().split()
    special = {'ii', 'iii', 'iv', 'vi', 'ix', 'xl', 'xc', 'cd', 'cm', 'mcm', 'mm', 'mmm'}
    result = []
    for word in words:
        if word in special:
            result.append(word.upper())
        elif word in {'of', 'and', 'or', 'with', 'for'}:
            result.append(word)
        else:
            result.append(word.capitalize())
    return ' '.join(result)

def find_block(identifier):
    """Find block by name or hex code."""
    try:
        start_code = parse_hex(identifier)
        for start, end, name in UNICODE_BLOCKS:
            if start == start_code:
                return start, end, name
    except ValueError:
        pass
    
    identifier_lower = identifier.lower()
    for start, end, name in UNICODE_BLOCKS:
        if identifier_lower in name.lower():
            return start, end, name
    
    if '-' in identifier:
        parts = identifier.split('-')
        if len(parts) == 2:
            try:
                start = parse_hex(parts[0])
                end = parse_hex(parts[1])
                return start, end, f"U+{start:04X}-U+{end:04X}"
            except ValueError:
                pass
    
    return None

def build_block(start, end, wrap, block_name, category):
    chars = []
    names = []

    for cp in range(start, end + 1):
        try:
            ch = chr(cp)
            name = unicodedata.name(ch)
            chars.append(ch)
            names.append(to_proper_case(name))
        except ValueError:
            continue

    if not chars:
        return None

    if wrap > 0:
        lines = [''.join(chars[i:i+wrap]) for i in range(0, len(chars), wrap)]
    else:
        lines = [''.join(chars)]
    preview_text = "\n" + "\n".join(lines)

    detail_lines = [f'«#00ff00»{ch}«»\t{name}' for ch, name in zip(chars, names)]
    detail_text = "\n".join(detail_lines)

    return {
        "name": block_name,
        "category": category,
        "civilopediaText": [
            {"size": 25, "padding": 1, "text": preview_text},
            {"separator": True},
            {
                "text": "This link opens the Compart Unicode block page in your browser. Copy characters or inspect the block there.",
                "link": f"https://www.compart.com/en/unicode/block/U+{start:04X}",
                "color": "#00FFFF",
                "size": 16,
            },
            {"size": 22, "text": detail_text},
        ]
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python uniblock.py <block_name_or_hex>")
        print("\nExamples:")
        print("  python uniblock.py 'Geometric Shapes'")
        print("  python uniblock.py 2500")
        print("  python uniblock.py 2500-257F")
        sys.exit(1)
    
    block_info = find_block(sys.argv[1])
    if not block_info:
        print(f"Block not found: {sys.argv[1]}")
        sys.exit(1)
    
    start, end, name = block_info
    block = build_block(start, end, WRAP, name, CATEGORY)
    
    if block is None:
        print(f"No valid characters found in range U+{start:04X}-U+{end:04X}")
        sys.exit(1)
    
    out_path = OUTPUT_DIR / f"uniblock_{start:04X}_{end:04X}.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    preview_text = block["civilopediaText"][0]["text"].lstrip("\n")
    detail_text = block["civilopediaText"][3]["text"].lstrip("\n")
    
    text = f'''    {{
        "name": "{block["name"]}",
        "category": "{block["category"]}",
        "civilopediaText": [
            {{ "size": 25,
              "padding": 1,
              "text": "
{preview_text}", }},

            {{ "separator": true }},
            {{  "text": "{block["civilopediaText"][2]["text"]}",
               "link": "{block["civilopediaText"][2]["link"]}",
               "color": "{block["civilopediaText"][2]["color"]}",
               "size": {block["civilopediaText"][2]["size"]}, }},

            {{ "size": 22, "text": "
{detail_text}", }},
        ]
    }},
'''
    
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    
    print(f"Wrote: {out_path}")

if __name__ == "__main__":
    main()