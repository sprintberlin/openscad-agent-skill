# Modeling patterns

- **Parameters first.** All dimensions as named variables at the top of the file.
- **Subtract with overshoot.** Make cutting bodies slightly larger than the part (e.g. `+0.01` on both ends) so faces are not coplanar.
- **2D to 3D.** Draw a profile with `square`, `circle`, `polygon`, then `linear_extrude(height=...)` or `rotate_extrude()`.
- **Modules.** One module per feature; call them from a short top-level assembly.
- **Clearance.** Add an explicit `clearance` variable for fits instead of baking tolerances into numbers.
- **Smooth curves.** Set `$fn` for visible round parts; keep it low for hidden features to keep renders fast.
- **Check with `-D`.** Try parameter variants from the command line before editing the file.
