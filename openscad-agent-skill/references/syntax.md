# OpenSCAD syntax cheat sheet

## 2D primitives

```openscad
circle(r = 10);              // or d = 20
square([w, h], center = true);
polygon(points = [[0,0],[40,0],[40,20],[0,30]]);
text("Hello", size = 10, font = "Arial", halign = "center");
```

## 3D primitives

```openscad
cube([w, d, h], center = true);
sphere(r = 10);              // or d = 20
cylinder(h = 30, r = 5);     // or d = 10
cylinder(h = 30, r1 = 5, r2 = 3);   // cone / frustum
polyhedron(points = [...], faces = [...]);
```

## Extrusion: 2D becomes 3D

```openscad
linear_extrude(height = 10) circle(d = 20);
linear_extrude(height = 30, twist = 90, slices = 40) square([10, 10]);
rotate_extrude(angle = 360) translate([15, 0]) circle(d = 4);   // torus-like
```

## Transformations

```openscad
translate([x, y, z]) ...
rotate([rx, ry, rz]) ...      // degrees around each axis
rotate(a = 45, v = [0,0,1]) ...
scale([x, y, z]) ...
resize([x, y, z]) ...
mirror([1, 0, 0]) ...
color("steelblue") ...
multmatrix(m) ...             // rarely needed; avoid
```

## Boolean operations

```openscad
union()        { ... }        // default; combine
difference()   { solid(); tool(); }   // first minus the rest
intersection() { ... }        // keep only the overlap
hull()         { ... }        // convex hull of children
minkowski()    { ... }        // dilation; slow, use sparingly
```

## Modules and functions

```openscad
module bracket(w = 40, t = 4) {
    cube([w, t, 30]);
}
function bolt_circle(r, n, i) = [r*cos(360*i/n), r*sin(360*i/n)];

bracket(w = 60);
```

- `use <lib.scad>` imports modules/functions only. `include <lib.scad>` also runs top-level code.
- Variables are set at compile time and behave like constants in their scope. Assignment is not a runtime mutation.
- `-D name=value` on the command line overrides a top-level variable without editing the file.

## Flow control

```openscad
for (i = [0:5]) translate([i*12, 0, 0]) cube(8);
for (a = [0:45:315]) rotate([0,0,a]) translate([20,0,0]) cylinder(h=5, d=4);
if (wall > 2) { ... } else { ... }
xs = [for (i = [1:10]) i*2];
```

## Resolution

```openscad
$fn = 64;    // fragments per full circle; 24 draft, 64 normal, 100+ fine
$fa = 5;     // minimum angle per fragment
$fs = 0.5;   // minimum fragment size
```

## Modifier characters (debugging)

```openscad
* cube(10);     // disable child
! sphere(10);   // show only this
# cylinder(10); // highlight transparent red
% cube(10);     // background ghost
```

## Import / projection

```openscad
import("part.stl");            // 3D: STL, OFF, AMF, 3MF
import("profile.dxf");         // 2D: DXF, SVG
projection(cut = true) ...     // 3D to 2D outline (or cross-section with cut=true)
```

## Text output for the agent

`echo()` prints to the console during compile. Use it to expose computed values:

```openscad
echo("inner width =", width - 2*wall);
```
