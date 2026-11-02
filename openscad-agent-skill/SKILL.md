---
name: openscad-agent-skill
description: "Model, modify and verify 2D and 3D parts with OpenSCAD; export STL, SVG, DXF or PNG."
---

# OpenSCAD modeling

1. Write a parametric `.scad` model. Check OpenSCAD output for errors and relevant warnings.
2. Export with `openscad -o part.stl part.scad` (3D), `openscad -o part.svg part.scad` or `openscad -o part.dxf part.scad` (2D). Overrides: `-D name=value`.
3. Render and visually inspect views appropriate to the geometry; correct and repeat. Example:
   ```sh
   openscad -o iso.png --imgsize=1200,900 --viewall --autocenter --camera=0,0,0,55,0,25,300 part.scad
   ```
   Camera rotations: top `0,0,0`, front `90,0,0`, side `90,0,90`, iso `55,0,25`; seven values are translation, rotation in degrees, distance.
4. Check dimensions against the requirements. On versions supporting it, use `--summary=bounding-box` on export. For an optional STL edge, bounding-box and volume check, run `python <skill-dir>/scripts/check_stl.py part.stl`; add `--expect-size X,Y,Z` when known. An edge check alone does not prove a mesh valid.
5. Report what was checked and any limitations.

References, relative to the skill directory: `references/install.md`, `references/syntax.md`, `references/patterns-2d.md`, `references/patterns-3d.md`, `references/libraries.md`, `references/pitfalls.md`.
