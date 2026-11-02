# Libraries worth using

Do not reimplement gears, threads and fillets. Use a library, and say in the file which one and which version.

## BOSL2 — first choice for general modeling

Shapes, rounding, attachments, screws, gears. Large but well documented.

```openscad
include <BOSL2/std.scad>
cuboid([50, 30, 20], rounding = 3);
```

- Repo: https://github.com/BelfrySCAD/BOSL2
- Wiki: https://github.com/BelfrySCAD/BOSL2/wiki
- License: BSD-2-Clause

## NopSCADlib — printer parts and electronics enclosures

```openscad
include <NopSCADlib/core.scad>
```

- Repo: https://github.com/nophead/NopSCADlib
- License: GPL-3.0 (attention: affects distributed models built on it)

## Round-Anything — filleted polygons

- Repo: https://github.com/Irev-Dev/Round-Anything
- License: MIT

## threads-scad — metric threads

- Repo: https://github.com/rcolyer/threads-scad
- License: CC0

## Installing

Put the library folder in the OpenSCAD library directory:

- Windows: `%USERPROFILE%\Documents\OpenSCAD\libraries\`
- macOS: `~/Documents/OpenSCAD/libraries/`
- Linux: `~/.local/share/OpenSCAD/libraries/`

Then `include <BOSL2/std.scad>` resolves. Alternatively keep the library next to the model and use a relative include.

**Rule for agents:** if a library is missing, say so and install it or vendor it. Do not silently substitute an approximation that changes the geometry.

**License note:** some libraries (NopSCADlib, STEMFIE) are GPL. For models that will be shared, prefer BOSL2, Round-Anything or threads-scad.
