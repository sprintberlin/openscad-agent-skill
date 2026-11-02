#!/usr/bin/env python3
"""Render standard views of an OpenSCAD file to PNG (headless).

Usage:
    python render_views.py part.scad --out views [-D name=value ...] [--size 1200,900]
                           [--views top,front,side,iso]

Prints one line per written file. Exit code is non-zero if OpenSCAD fails or an
image is missing or empty. Python standard library only.
"""
import argparse
import os
import shutil
import subprocess
import sys

# View name -> camera rotation (degrees). Translate and distance are fitted
# automatically by --viewall --autocenter.
VIEWS = {
    "top": "0,0,0",
    "front": "90,0,0",
    "side": "90,0,90",
    "iso": "55,0,25",
}


def find_openscad():
    exe = shutil.which("openscad")
    if exe:
        return exe
    candidates = [
        r"C:\Program Files\OpenSCAD\openscad.exe",
        r"C:\Program Files (x86)\OpenSCAD\openscad.exe",
        "/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD",
        "/usr/bin/openscad",
        "/snap/bin/openscad",
    ]
    for c in candidates:
        if os.path.isfile(c):
            return c
    sys.exit("OpenSCAD not found. Install it (see references/install.md) or put it on PATH.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scad", help="input .scad file")
    ap.add_argument("--out", default="views", help="output folder (default: views)")
    ap.add_argument("--size", default="1200,900", help="image size W,H (default 1200,900)")
    ap.add_argument("--views", default="top,front,side,iso", help="comma list from: " + ",".join(VIEWS))
    ap.add_argument("-D", dest="defs", action="append", default=[], metavar="name=value",
                    help="override a top-level variable (repeatable)")
    args = ap.parse_args()

    if not os.path.isfile(args.scad):
        sys.exit("File not found: " + args.scad)
    names = [v.strip() for v in args.views.split(",") if v.strip()]
    unknown = [v for v in names if v not in VIEWS]
    if unknown:
        sys.exit("Unknown view(s): %s. Choose from: %s" % (", ".join(unknown), ", ".join(VIEWS)))

    exe = find_openscad()
    os.makedirs(args.out, exist_ok=True)
    base = os.path.splitext(os.path.basename(args.scad))[0]
    failed = False

    for name in names:
        out = os.path.join(args.out, "%s_%s.png" % (base, name))
        cmd = [exe, "-o", out, "--imgsize=" + args.size, "--viewall", "--autocenter",
               "--projection=perspective", "--camera=0,0,0,%s,300" % VIEWS[name]]
        for d in args.defs:
            cmd += ["-D", d]
        cmd.append(args.scad)
        proc = subprocess.run(cmd, capture_output=True, text=True)
        ok = proc.returncode == 0 and os.path.isfile(out) and os.path.getsize(out) > 0
        if proc.stderr.strip():
            # OpenSCAD logs warnings and ECHO output on stderr; surface them.
            for line in proc.stderr.strip().splitlines():
                print("  [openscad] " + line)
        if ok:
            print("%s -> %s (%d bytes)" % (name, out, os.path.getsize(out)))
        else:
            failed = True
            print("%s FAILED (exit %d)" % (name, proc.returncode), file=sys.stderr)

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
