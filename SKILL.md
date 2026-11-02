---
name: openscad-agent-skill
description: "Model 2D and 3D parts in OpenSCAD and verify them by rendering views and inspecting the images before reporting success. Use when asked to design, modify or check a parametric part, enclosure, bracket or 2D profile with OpenSCAD, and export STL, PNG or SVG."
---

# OpenSCAD 2D & 3D modeling for AI agents

A model is only verified after its rendered views have been looked at. A file that exports without error can still have the wrong shape, the wrong side or a missing cut-out.

## Loop

1. **Find OpenSCAD.** Run `openscad --version`. If it is not on PATH, see `references/install.md`.
2. **Write the part** as a parametric `.scad` file in a working folder outside this skill.
   - Every dimension is a named variable at the top. Set `$fn` (e.g. 64) for round parts.
   - Patterns and pitfalls: `references/modeling-patterns.md`, `references/pitfalls.md`.
3. **Export.** `openscad -o part.stl part.scad` (3D) or `openscad -o part.svg part.scad` (2D). Check the file exists and is not empty.
4. **Render several views** to PNG. Camera syntax and the standard view set: `references/render-views.md`.
5. **Look at every PNG** with the image-viewing or vision capability of your agent. Compare against the request: overall shape, holes and cut-outs in the right place, right side open, not an empty or single-colour image.
6. **Correct and repeat** steps 2-5. Try parameter changes without editing the file: `-D name=value`.
7. **Report** only after step 5. Say which views were inspected and what was checked.

## Rules

- Do not judge a model from a view you did not intend. If the image is not the requested view, fix `--camera` first.
- Keep the working folder, not the skill folder, as output location.
- Do not claim dimensions are right from the image alone. Check them against the variables in the file.
- Examples in `examples/` were rendered and inspected; reuse them as starting points.

## Scope

Modeling and verification only. Slicing and printing are out of scope.
