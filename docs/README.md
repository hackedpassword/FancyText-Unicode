# Useful Unciv Unicode info

In-game Unicode symbols are statically mapped to special images, defined here:
https://github.com/yairm210/Unciv/blob/master/core/src/com/unciv/ui/components/fonts/Fonts.kt#L118

These symbols are altered from their standard form, with new images, seen here:
https://github.com/yairm210/Unciv/tree/master/android/ImagesToNotAddToGame

## 1. All Unciv Unicode symbols
```
⏳ † ‡ ➡ … ♡ ⚙ ¤ ⁂ ⍾ ♪ ⌣ ☮ ♬ ⚒ ⛤ ⚖ ⚛ ☠ ⛏ ∞ ⌚ ✯ ◉ ￪ ￬ →
```

## 2. Markdown table derived from code
| Char | Var | Description | ID | Block range | Block name |
| :---: | :--- | :--- | :--- | :--- | :--- |
| ⏳ | turn | hourglass with flowing sand | U+23F3 | U+2300–U+23FF | Miscellaneous Technical |
| † | strength | dagger | U+2020 | U+2000–U+206F | General Punctuation |
| ‡ | rangedStrength | double dagger | U+2021 | U+2000–U+206F | General Punctuation |
| ➡ | movement | black rightwards arrow | U+27A1 | U+2700–U+27BF | Dingbats |
| … | range | horizontal ellipsis | U+2026 | U+2000–U+206F | General Punctuation |
| ♡ | health | white heart suit | U+2661 | U+2600–U+26FF | Miscellaneous Symbols |
| ⚙ | production | gear | U+2699 | U+2600–U+26FF | Miscellaneous Symbols |
| ¤ | gold | currency sign | U+00A4 | U+0080–U+00FF | Latin-1 Supplement |
| ⁂ | food | asterism (alt: 🍏 U+1F34F green apple) | U+2042 | U+2000–U+206F | General Punctuation |
| ⍾ | science | bell symbol (alt: 🧪 U+1F9EA test tube, 🔬 U+1F52C microscope) | U+237E | U+2300–U+23FF | Miscellaneous Technical |
| ♪ | culture | eighth note (alt: 🎵 U+1F3B5 musical note) | U+266A | U+2600–U+26FF | Miscellaneous Symbols |
| ⌣ | happiness | smile (alt: 😀 U+1F600 grinning face) | U+2323 | U+2300–U+23FF | Miscellaneous Technical |
| ☮ | faith | peace symbol (alt: 🕊 U+1F54A dove of peace) | U+262E | U+2600–U+26FF | Miscellaneous Symbols |
| ♬ | greatArtist | sixteenth note | U+266C | U+2600–U+26FF | Miscellaneous Symbols |
| ⚒ | greatEngineer | hammer | U+2692 | U+2600–U+26FF | Miscellaneous Symbols |
| ⛤ | greatGeneral | pentagram | U+26E4 | U+2600–U+26FF | Miscellaneous Symbols |
| ⚖ | greatMerchant | scale | U+2696 | U+2600–U+26FF | Miscellaneous Symbols |
| ⚛ | greatScientist | atom | U+269B | U+2600–U+26FF | Miscellaneous Symbols |
| ☠ | death | skull and crossbones | U+2620 | U+2600–U+26FF | Miscellaneous Symbols |
| ⛏ | automate | pick | U+26CF | U+2600–U+26FF | Miscellaneous Symbols |
| ∞ | infinity | infinity | U+221E | U+2200–U+22FF | Mathematical Operators |
| ⌚ | clock | watch | U+231A | U+2300–U+23FF | Miscellaneous Technical |
| ✯ | star | pinwheel star | U+272F | U+2700–U+27BF | Dingbats |
| ◉ | status | fisheye | U+25C9 | U+25C0–U+25FF | Geometric Shapes |
| ￪ | sortUpArrow | half wide upward arrow | U+FFEA | U+FF00–U+FFEF | Halfwidth and Fullwidth Forms |
| ￬ | sortDownArrow | half wide downward arrow | U+FFEC | U+FF00–U+FFEF | Halfwidth and Fullwidth Forms |
| → | rightArrow | rightwards arrow | U+2192 | U+2190–U+21FF | Arrows |

## 3. Aggregate list of block ranges (with counts)
- **U+2600–U+26FF** (Miscellaneous Symbols) – **11** entries  
  (health, production, culture, faith, greatArtist, greatEngineer, greatGeneral, greatMerchant, greatScientist, death, automate)
- **U+2300–U+23FF** (Miscellaneous Technical) – **4** entries  
  (turn, science, happiness, clock)
- **U+2000–U+206F** (General Punctuation) – **4** entries  
  (strength, rangedStrength, range, food)
- **U+2700–U+27BF** (Dingbats) – **2** entries  
  (movement, star)
- **U+FF00–U+FFEF** (Halfwidth and Fullwidth Forms) – **2** entries  
  (sortUpArrow, sortDownArrow)
- **U+0080–U+00FF** (Latin-1 Supplement) – **1** entry  
  (gold)
- **U+2200–U+22FF** (Mathematical Operators) – **1** entry  
  (infinity)
- **U+25C0–U+25FF** (Geometric Shapes) – **1** entry  
  (status)
- **U+2190–U+21FF** (Arrows) – **1** entry  
  (rightArrow)

## 4. Aggregate table symbol listing
| block range      | block name                            | chars                 |
| :--------------- | :------------------------------------ | :-------------------- |
| U+0080..U+00FF   | Latin-1 Supplement                    | ¤                     |
| U+2000..U+206F   | General Punctuation                   | † ‡ … ⁂               |
| U+2190..U+21FF   | Arrows                                | ↑ ↓ →                 |
| U+2200..U+22FF   | Mathematical Operators                | ∞                     |
| U+2300..U+23FF   | Miscellaneous Technical               | ⏳ ⍾ ⌣ ⌚               |
| U+25A0..U+25FF   | Geometric Shapes                      | ◉                     |
| U+2600..U+26FF   | Miscellaneous Symbols                 | ♡ ⚙ ♪ ☮ ♬ ⚒ ⛤ ⚖ ⚛ ☠ ⛏ |
| U+2700..U+27BF   | Dingbats                              | ➡ ✯                   |
| U+1F300..U+1F5FF | Miscellaneous Symbols and Pictographs | 🍏 🔬 🎵 🕊           |
| U+1F600..U+1F64F | Emoticons                             | 😀                    |
| U+1F900..U+1F9FF | Supplemental Symbols and Pictographs  | 🧪                    |
| U+FF00..U+FFEF   | Halfwidth and Fullwidth Forms         | ￪ ￬                   |
