# Pitfalls

- Coplanar faces in `difference()` can cause artifacts. Extend the cutting body past the surface.
- Low circle resolution causes facets; adjust `$fn`, `$fa` or `$fs`.
- Camera rotation `0,0,0` is a top view.
- For installation and PATH, see `install.md`.
- `use <lib>` imports modules and functions; `include <lib>` also runs top-level code.
- Variables are compile-time values within their scope, not runtime mutations.
- Check questionable imported meshes before booleans; `scripts/check_stl.py` checks edge counts, not full mesh validity.
- `minkowski()` can be slow; `hull()` or a library may be faster.
