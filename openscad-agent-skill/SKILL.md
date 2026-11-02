---
name: openscad-agent-skill
description: "Model 2D and 3D parts in OpenSCAD and verify them by rendering views and inspecting the images before reporting success. Use when asked to design, modify or check a parametric part, enclosure, bracket, holder or 2D profile with OpenSCAD, and export STL, PNG, SVG or DXF."
---

# OpenSCAD 2D & 3D modeling for AI agents

A model is only verified after its rendered views have been looked at. A file that exports without error can still have the wrong shape, the wrong side or a missing cut-out.

## The loop

1. **Find OpenSCAD.** Run `openscad --version`. Not on PATH: see `references/install.md`.
2. **Write the part** as a parametric `.scad` file in a working folder outside this skill.
   - Every dimension is a named variable at the top. Set `$fn` (e.g. 64) for round parts.
   - Read what you need, not everything:
     - Syntax cheat sheet: `references/syntax.md`
     - 2D profiles and text: `references/patterns-2d.md`
     - 3D construction (shells, holes, fits, brackets): `references/patterns-3d.md`
     - Reusable libraries (BOSL2, NopSCADlib, threads): `references/libraries.md`
3. **Export.** `openscad -o part.stl part.scad` (3D) or `openscad -o part.svg part.scad` (2D). Check the file exists and is not empty. Read OpenSCAD's stderr: warnings about unknown variables or ambiguous operations are errors in disguise.
4. **Check geometry** for 3D parts: `python scripts/check_stl.py part.stl`. Expect a closed mesh, a sensible bounding box and positive volume. An open mesh means the model is wrong, not the export.
5. **Render several views** to PNG: `python scripts/render_views.py part.scad --out views` (top, front, side, iso). Camera syntax: `references/render-views.md`.
6. **Look at every PNG** with the image-viewing or vision capability of your agent. Compare against the request: overall shape, holes and cut-outs in the right place, right side open, not an empty or single-colour image.
7. **Correct and repeat** steps 2-6. Try parameter changes without editing the file: `-D name=value`.
8. **Report** only after step 6. Say which views were inspected, what the geometry check reported and what you verified against the request.

## Rules

- Do not judge a model from a view you did not intend. If the image is not the requested view, fix `--camera` first.
- Keep the working folder, not the skill folder, as output location.
- Do not claim dimensions are right from the image alone. Check them against the variables in the file and the STL bounding box.
- Prefer boring, readable geometry over clever one-liners. The next edit should be easy.
- Examples in `examples/` were rendered and inspected; reuse them as starting points, not as fixed designs.
- Common traps: `references/pitfalls.md`.

## Scope

Modeling and verification only. Slicing and printing are out of scope.
