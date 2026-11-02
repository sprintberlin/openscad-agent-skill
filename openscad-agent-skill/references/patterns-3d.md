# 3D patterns

## Open box

```openscad
module open_box(size = [80, 50, 30], wall = 2) {
    difference() {
        cube(size);
        translate([wall, wall, wall]) cube([size[0] - 2*wall, size[1] - 2*wall, size[2]]);
    }
}
```

The inner cube is `size[2]` tall from z = wall, so it exits the top face. No coplanar faces.

## Holes

```openscad
module through_hole(d = 3.2, h = 20) cylinder(h = h + 0.02, d = d, center = true);

module counterbore(d = 3.2, head_d = 6, head_h = 3, h = 20) {
    through_hole(d, h);
    translate([0, 0, h/2 - head_h]) cylinder(h = head_h + 0.01, d = head_d);
}

module slot(length = 20, d = 4, h = 10) {
    hull() for (x = [-length/2 + d/2, length/2 - d/2])
        translate([x, 0, 0]) cylinder(h = h, d = d, center = true);
}
```

## Fit

```openscad
clearance = 0.3;                      // per side
socket_d = part_d + 2*clearance;
```

## Rounded box

```openscad
module rounded_box(size = [60, 40, 20], r = 4) {
    translate([size[0]/2, size[1]/2, 0])
        linear_extrude(height = size[2]) rounded_rect([size[0], size[1]], r);   // from references/patterns-2d.md
}
```

## Holder (angled support)

- Base wider than the supported object.
- Gusset or fillet at the base-to-support joint.
- Retaining lip clears the object on insertion.

## Section switch

```openscad
section = false;
module model() { /* part */ }
if (section)
    intersection() { model(); translate([-1000, 0, -1000]) cube(2000); }
else
    model();
```

`-D section=true` renders the front half; the cut face shows walls and internal features.

## Imported mesh

`import("part.stl")` for booleans and remixes. Check questionable meshes before use.
