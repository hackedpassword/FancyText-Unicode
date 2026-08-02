# ⚑ FancyText Unicode ⚑

## What is this?

A two part mod:
1. Prepend cities with a symbol relative to their type for better management,
2. Visualizing unicode characters via a Tutorials menu section that can be used for modding or unit/city naming.

In-game, this is what you'd see in the spy screen for example - notice capitals and CS's are clearly marked:

![](https://raw.githubusercontent.com/hackedpassword/Unciv-Assets/refs/heads/main/Images/FancytextUnicode/fancytextUnicode_example.png)

## Why could this be helpful?

Unicode is notoriously variable on rendering symbols, per screen, per platform, etc.

⚠ For example, the map editor cannot render certain symbols, while the tutorials screen can. Android and Windows do not have a unified font base.

[PR#15166](https://github.com/yairm210/Unciv/pull/15166) addressed one such issue lately. Alternative solutions to font rendering issues might be addressed by a mod like [SomeTroglodyte/Sort-Icons](https://github.com/SomeTroglodyte/Sort-Icons).

💡 New: There are now Resources named with symbols from the Arrows block (U+2190) and a test render map. Glyph resources enable render testing in Editor and World screens.

## How to use

1. Start a new game, G&K base
2. Select FancytextUnicode as an add-on mod
3. Start the game

Now if you press F1 or tap to Civilopedia, under the *Tutorials* section, you will see a new `FancyText Unicode` section. The subsections demonstrate various symbols.

⚠ Symbols that render in tutorials may not render in another screen.


# Preview of Tutorial.json

## Make city names more referential

**Using symbols in unit or city names adds a fun and readable attribute! ♬**



All capitol cities ⭐ and city-states ⟰ in this mod have a symbol prefix.



Aliased cities look like:

Babylon = ⭐Babylon<br>Athens = ⭐Athens<br>Beijing = ⭐Beijing<br>...<br>Brussels = ⟰Brussels<br>Bucharest = ⟰Bucharest<br>Florence = ⟰Florence<br>...

<a href="https://github.com/hackedpassword/FancyText-Unicode/blob/main/jsons/translations/English.properties" style="color:#00FFFF; font-size:16px">See: jsons/English.properties</a>



---

## Uses: City/Unit names



⚔ Improve *sorting* city/unit names and labels in various screens and menus!

⚔ Better unit identification at-a-glance!



## Uses: Examples



By adding a symbol prefix to a name:



❈ The spy_screen cities will auto-sort based on Capitols and CS's

❈ The city_screen [city name] reveals if this city is a CS or Capitol

❈ The unit_screen can auto-sort by special cities



By adding prefix symbol badges to high ranking units, this helps manage unit strategy faster.

Different unit types or groups can be assigned their own ranks (manually of course, just another way to crawl).



## Uses: Advanced assets



An even more clever use is for naming mod assets in very unique ways.



Rather than a long description, a unicode symbol says it all, i.e.:<br>  ⮝ ╦.png



..says this asset has reduced a descriptive name from 5 words to 2 symbols, describing an upper aligned top-to-bottom T-intersection.



Add unit prefixes like in these examples:

☮ Great Prophet<br>⚛ GDR Boss<br>⚍ Lt Cmdr<br>⛉⛉⛉ Sky Admiral (3rd rank)<br>⚑⭐ Washington (the additional flag tells me this is _my_ capital city, vs _other_ captured capitals)



---

###### ☣ Gotchas ☣



  ☹ Copying characters? There does not appear to be a way to highlight-select text in-game, other than from city or unit renaming.

  ☹ <span style="color:#ff0000">You cannot copy characters from this help screen!</span> See below.

  ☹ 😝 ☹ 😛 ← the Emoji Faces (Smileys) pictograph set doesn't work. Other basic emojis do ☠ ☺



---



**To use these symbols for your cities or units:**

▸ <span style="color:#00FFFF">tap the link</span> under the sections' preview block which opens Firefox etc,<br>▸ <span style="color:#00FFFF">copy the symbol</span> from your browser,<br>▸ <span style="color:#00FFFF">paste into an Unciv textbox</span> from in-game.



The FancyText sections here are known good rendering Unicode blocks. Pictograph symbols generally don't work. More sections to be added.

