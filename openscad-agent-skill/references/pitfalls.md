# Pitfalls

- Coplanar faces in `difference()` leave a skin or flicker. Extend the cutting body by 0.01 mm or more past the surface.
- Default `$fn` gives faceted circles. Set `$fn`.
- Wrong camera: rotation `0,0,0` is a top view.
- Windows: the installer does not add OpenSCAD to PATH. See `install.md`.
- `use <lib>` imports modules and functions only; `include <lib>` also runs top-level code.
- Top-level variables are constants within their scope. They are not reassigned at runtime.
- Imported STL with an open mesh breaks booleans silently. Run `scripts/check_stl.py` on it first.
- `minkowski()` is slow. Use `hull()` of primitives or BOSL2 rounding.
