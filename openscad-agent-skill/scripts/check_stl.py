#!/usr/bin/env python3
"""Basic geometry check for an STL file (ASCII or binary).

Usage:
    python check_stl.py part.stl [--expect-size X,Y,Z] [--tol 0.5]

Reports triangle count, bounding box, volume and whether the mesh is closed
(every edge shared by exactly two triangles). Exit code 1 if the mesh is open,
the volume is not positive, or --expect-size does not match within --tol (mm).
Python standard library only.
"""
import argparse
import struct
import sys


def read_stl(path):
    with open(path, "rb") as f:
        data = f.read()
    if len(data) >= 84:
        n = struct.unpack("<I", data[80:84])[0]
        if 84 + 50 * n == len(data):
            tris = []
            off = 84
            for _ in range(n):
                v = struct.unpack("<12f", data[off:off + 48])
                tris.append(((v[3], v[4], v[5]), (v[6], v[7], v[8]), (v[9], v[10], v[11])))
                off += 50
            return tris
    # ASCII
    text = data.decode("utf-8", errors="replace")
    verts = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("vertex"):
            p = s.split()
            verts.append((float(p[1]), float(p[2]), float(p[3])))
    if not verts or len(verts) % 3:
        sys.exit("Could not parse STL: %s" % path)
    return [tuple(verts[i:i + 3]) for i in range(0, len(verts), 3)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stl")
    ap.add_argument("--expect-size", help="expected bounding box X,Y,Z in mm")
    ap.add_argument("--tol", type=float, default=0.5, help="tolerance in mm (default 0.5)")
    args = ap.parse_args()

    tris = read_stl(args.stl)
    xs = [v[0] for t in tris for v in t]
    ys = [v[1] for t in tris for v in t]
    zs = [v[2] for t in tris for v in t]
    size = (max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs))

    # Signed volume via divergence theorem.
    vol = 0.0
    for a, b, c in tris:
        vol += (a[0] * (b[1] * c[2] - b[2] * c[1])
                - a[1] * (b[0] * c[2] - b[2] * c[0])
                + a[2] * (b[0] * c[1] - b[1] * c[0])) / 6.0

    # Closed mesh: each undirected edge appears exactly twice.
    def key(p):
        return (round(p[0], 4), round(p[1], 4), round(p[2], 4))

    edges = {}
    for a, b, c in tris:
        for p, q in ((a, b), (b, c), (c, a)):
            k = tuple(sorted((key(p), key(q))))
            edges[k] = edges.get(k, 0) + 1
    bad = sum(1 for n in edges.values() if n != 2)
    closed = bad == 0

    print("triangles : %d" % len(tris))
    print("bbox (mm) : %.3f x %.3f x %.3f" % size)
    print("min corner: %.3f, %.3f, %.3f" % (min(xs), min(ys), min(zs)))
    print("volume    : %.3f mm3" % vol)
    print("closed    : %s%s" % ("yes" if closed else "NO", "" if closed else " (%d bad edges)" % bad))

    problems = []
    if not closed:
        problems.append("mesh is not closed")
    if vol <= 0:
        problems.append("volume is not positive")
    if args.expect_size:
        exp = tuple(float(x) for x in args.expect_size.split(","))
        if len(exp) != 3:
            sys.exit("--expect-size needs X,Y,Z")
        for axis, got, want in zip("XYZ", size, exp):
            if abs(got - want) > args.tol:
                problems.append("%s size %.3f differs from expected %.3f" % (axis, got, want))
    if problems:
        print("RESULT    : FAIL - " + "; ".join(problems))
        sys.exit(1)
    print("RESULT    : OK")


if __name__ == "__main__":
    main()
