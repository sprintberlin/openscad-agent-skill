# Install OpenSCAD

- Windows: download the current snapshot installer from <https://files.openscad.org/snapshots/> (`OpenSCAD-<date>-x86-64-Installer.exe`, silent switch `/S`). It installs to `C:\Program Files\OpenSCAD (Nightly)`; add that to PATH. `winget` ships only the old 2021.01 release.
- macOS: `brew install openscad` (2021.01) or the snapshot `.dmg` from the same page.
- Debian/Ubuntu: `sudo apt install openscad` or the snapshot `.AppImage`.

Check: `openscad --version`. 2021.01 works for everything in this skill; current snapshots are faster (Manifold geometry engine) and verified too.
