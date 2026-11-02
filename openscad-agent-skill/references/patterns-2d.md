# 2D construction patterns

2D work is not a lesser 3D. Profiles, outlines, gaskets, panels, engraving and cross-section checks all start here.

## Rounded rectangle without a library

```openscad
module rounded_rect(size = [80, 50], r = 5) {
    offset(r = r) offset(r = -r) square(size, center = true);
}
```

Or with hull of four circles — predictable and cheap:

```openscad
module rounded_rect(size = [80, 50], r = 5) {
    hull() {
        for (x = [-size[0]/2 + r, size[0]/2 - r])
            for (y = [-size[1]/2 + r, size[1]/2 - r])
                translate([x, y]) circle(r = r);
    }
}
```

## Outline as polygon

Use `polygon` when the outline is the design. Keep points in one list variable at the top.

```openscad
outline = [[0,0],[70,0],[70,12],[12,12],[12,60],[0,60]];
polygon(outline);
```

## Subtract before you extrude

Holes and slots belong in the 2D profile when they go all the way through:

```openscad
linear_extrude(height = 4)
difference() {
    rounded_rect([80, 50], r = 5);
    circle(d = 20);
    for (x = [-30, 30]) translate([x, 0]) circle(d = 4);
}
```

## Text and engraving

```openscad
text("M3", size = 6, halign = "center", valign = "center");
```

- Check that the font exists on the machine. Default to a common font or leave `font` unset.
- For engraving, extrude the text shallowly and subtract it from the plate.

## Export

- SVG: `openscad -o part.svg part.scad`
- DXF: `openscad -o part.dxf part.scad`
- A 2D file renders top-down by definition. Still look at the PNG: mirrored text and missing holes are easy to miss in code.

## Cross-section of a 3D part

`projection(cut = true)` at a chosen Z gives a 2D slice. Useful to check wall thickness without slicing software:

```openscad
projection(cut = true) translate([0, 0, -5]) import("part.stl");
```
