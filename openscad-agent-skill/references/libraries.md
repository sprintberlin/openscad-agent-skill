# Libraries

| Library | Use | License |
|---|---|---|
| [BOSL2](https://github.com/BelfrySCAD/BOSL2) | shapes, rounding, attachments, screws, gears | BSD-2-Clause |
| [NopSCADlib](https://github.com/nophead/NopSCADlib) | printer parts, electronics, enclosures | GPL-3.0 |
| [Round-Anything](https://github.com/Irev-Dev/Round-Anything) | filleted polygons | MIT |
| [threads-scad](https://github.com/rcolyer/threads-scad) | metric threads | CC0 |

```openscad
include <BOSL2/std.scad>
cuboid([50, 30, 20], rounding = 3);
```

## Install

Place the library folder in:

- Windows: `%USERPROFILE%\Documents\OpenSCAD\libraries\`
- macOS: `~/Documents/OpenSCAD/libraries/`
- Linux: `~/.local/share/OpenSCAD/libraries/`

Or keep it next to the model and include by relative path.

## Notes

- Note the library and version in a comment at the top of the file.
