# Rendering views headless

Verified with OpenSCAD 2021.01 on Windows. The same options exist on Linux and macOS.

```
openscad -o view.png --imgsize=1200,900 --viewall --autocenter \
  --projection=perspective --camera=TX,TY,TZ,RX,RY,RZ,DIST part.scad
```

`--camera` takes **7 numbers**: translate x,y,z, then rotate x,y,z in degrees, then distance. It is not eye/center. Rotation `0,0,0` is a top-down view, so passing eye coordinates in the first three slots silently produces a top view.

Standard set (change only the rotation, one output file per view):

| View  | Rotation |
|-------|----------|
| top   | `0,0,0`  |
| front | `90,0,0` |
| side  | `90,0,90`|
| iso   | `55,0,25`|

Example iso: `--camera=0,0,0,55,0,25,300`.

With `--viewall --autocenter` the translate and distance values are fitted automatically; only the rotation matters for choosing the view.

Default colours are readable in vision checks. Change them only on request.
