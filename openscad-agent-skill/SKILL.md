---
name: openscad-agent-skill
description: "Model 2D and 3D parts in OpenSCAD and verify them by rendering views and inspecting the images. Use when asked to design, modify or check a parametric part, enclosure, bracket, holder or 2D profile with OpenSCAD, or to export STL, SVG, DXF or PNG."
---

# OpenSCAD modeling

Report a model as done only after viewing its renders.

## Workflow

1. `openscad --version`. Not found: `references/install.md`.
2. Write `part.scad` in a working folder.
   - Dimensions as named variables at the top; `$fn = 64` for round parts.
   - References: `references/syntax.md`, `references/patterns-2d.md`, `references/patterns-3d.md`, `references/libraries.md`, `references/pitfalls.md`.
3. Export.
   - 3D: `openscad -o part.stl part.scad`
   - 2D: `openscad -o part.svg part.scad` or `part.dxf`
   - Read the output and resolve warnings (the exit code stays 0). A 3D export reports `Status: NoError`.
4. Render four views.
   ```
   openscad -o top.png   --imgsize=1200,900 --viewall --autocenter --camera=0,0,0,0,0,0,300   part.scad
   openscad -o front.png --imgsize=1200,900 --viewall --autocenter --camera=0,0,0,90,0,0,300  part.scad
   openscad -o side.png  --imgsize=1200,900 --viewall --autocenter --camera=0,0,0,90,0,90,300 part.scad
   openscad -o iso.png   --imgsize=1200,900 --viewall --autocenter --camera=0,0,0,55,0,25,300 part.scad
   ```
   `--camera` = translate x,y,z, rotate x,y,z (degrees), distance. Rotation `0,0,0` is a top view. With `--viewall --autocenter` only the rotation matters.
5. View every PNG. Check shape, holes, cut-outs, open side. An empty or single-colour image means nothing is in view.
6. Optional geometry check: `python scripts/check_stl.py part.stl --expect-size X,Y,Z` (closed mesh, bounding box, volume). Useful because OpenSCAD's CLI cannot check the mesh or dimensions.
7. Fix and repeat. Override a variable without editing: `-D name=value`.
8. Report which views were checked and any geometry-check result.
