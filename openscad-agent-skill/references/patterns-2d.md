# 2D patterns

## Rounded rectangle

```openscad
module rounded_rect(size = [80, 50], r = 5) {
    hull() for (x = [-size[0]/2 + r, size[0]/2 - r], y = [-size[1]/2 + r, size[1]/2 - r])
        translate([x, y]) circle(r = r);
}
```

## Outline as polygon

```openscad
outline = [[0,0],[70,0],[70,12],[12,12],[12,60],[0,60]];
polygon(outline);
```

## Holes in the profile, then extrude

```openscad
linear_extrude(height = 4)
difference() {
    rounded_rect([80, 50], r = 5);
    circle(d = 20);
    for (x = [-30, 30]) translate([x, 0]) circle(d = 4);
}
```

## Text

```openscad
text("M3", size = 6, halign = "center", valign = "center");
```

- Unset `font` uses the system default. A missing font logs a warning.
- Engraving: `linear_extrude(0.6) text(...)` subtracted from the plate.

## Export

- `openscad -o part.svg part.scad`
- `openscad -o part.dxf part.scad`
- A 2D export is a top view. Render the PNG to check mirrored text and missing holes.

## Cross-section of a 3D part

```openscad
projection(cut = true) translate([0, 0, -5]) import("part.stl");
```

The slice at z = 5 mm shows wall thickness.
