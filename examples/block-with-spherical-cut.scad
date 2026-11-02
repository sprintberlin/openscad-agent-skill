// Block with a spherical cut-out. Rendered and inspected with OpenSCAD 2021.01.
$fn = 64;
block = [60, 40, 20];
sphere_d = 30;

difference() {
    cube(block);
    translate([block[0]/2, block[1]/2, block[2] + 5]) sphere(d = sphere_d);
}
