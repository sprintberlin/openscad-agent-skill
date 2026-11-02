# 3D construction patterns

## Hollow shell (box, enclosure)

Subtract an inner box that is taller than the outer one. Never make inner and outer faces coplanar.

```openscad
module shell(size = [80, 50, 30], wall = 2) {
    difference() {
        cube(size);
        translate([wall, wall, wall])
            cube([size[0]-2*wall, size[1]-2*wall, size[2]]);  // open top
    }
}
```

The top overshoot comes from using `size[2]` unreduced for the inner height.

## Holes, counterbores, slots

```openscad
module through_hole(d = 3.2, h = 20) cylinder(h = h + 0.02, d = d, center = true);

module counterbore(d = 3.2, head_d = 6, head_h = 3, h = 20) {
    through_hole(d, h);
    translate([0, 0, h/2 - head_h]) cylinder(h = head_h + 0.01, d = head_d);
}

module slot(length = 20, d = 4, h = 10) {
    hull() {
        for (x = [-length/2 + d/2, length/2 - d/2])
            translate([x, 0, 0]) cylinder(h = h, d = d, center = true);
    }
}
```

## Fits and clearance

Do not bake tolerances into every number. One variable controls the fit:

```openscad
clearance = 0.3;        // per side, adjust to the process
socket_d = part_d + 2*clearance;
```

State in the file comment whether clearance is per side or diametral.

## Brackets and holders

Build from a stable base, a support and a retaining feature. Think about where the load goes:

- The base carries the load; make it wide enough not to tip.
- Supports at an angle need a fillet or gusset at the joint, not a knife edge.
- A retaining lip must clear the object during insertion, not only in the final pose.

## Fillets without a library

A cheap vertical-edge fillet on a box:

```openscad
module rounded_box(size = [60, 40, 20], r = 4) {
    linear_extrude(height = size[2])
        rounded_rect([size[0], size[1]], r);   // see patterns-2d.md
}
```

For true 3D rounds use BOSL2 (`libraries.md`) instead of hand-rolled Minkowski sums.

## Cutaway view inside the model

Add a `section` switch so the agent can see inside without editing geometry:

```openscad
section = false;
module model() { /* the part */ }

if (section) {
    intersection() {
        model();
        translate([-1000, 0, -1000]) cube([2000, 1000, 2000]);  // keep front half
    }
} else {
    model();
}
```

Render once with `-D section=true` to inspect walls and internal features.

## Import and repair

`import("part.stl")` works for booleans and remixes. Check an imported mesh with `scripts/check_stl.py` before building on it; a non-closed import produces silent boolean failures.
