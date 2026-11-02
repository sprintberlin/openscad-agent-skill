# Installing OpenSCAD

- **Windows:** `winget install --id OpenSCAD.OpenSCAD --accept-source-agreements --accept-package-agreements --silent --disable-interactivity`
  The installer does not add OpenSCAD to PATH. Call it by full path, e.g. in PowerShell `& 'C:\Program Files\OpenSCAD\openscad.exe' --version`. (Verified: installs version 2021.01.)
- **macOS:** `brew install openscad`
- **Debian/Ubuntu:** `sudo apt install openscad`

Check with `openscad --version`. Older releases (2021.01) work for everything in this skill. Newer development builds add features but are not required.
