# Pitfalls

- **Wrong camera = wrong conclusion.** `--camera` rotation `0,0,0` is a top view. See `render-views.md`.
- **Coplanar faces.** A subtracted body that ends exactly on a surface leaves a thin skin or flicker. Overshoot the cut.
- **Low `$fn`.** The default makes circles visibly faceted. Set `$fn`.
- **Export succeeded is not verified.** Always look at rendered views.
- **Not on PATH (Windows).** Call `openscad.exe` by full path.
- **Empty render.** An all-background image usually means nothing is in view or the model is empty. Check the camera and the top-level geometry.
