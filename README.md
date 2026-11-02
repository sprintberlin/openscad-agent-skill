# openscad-agent-skill

A skill for AI agents (OpenClaw, Hermes, Claude Code and others that read `SKILL.md`) that teaches 2D and 3D modeling with OpenSCAD with one rule: **a model counts as done only after its rendered views were inspected.**

## Layout

```
openscad-agent-skill/            # the skill folder
  SKILL.md                       # the loop: model, export, check, render, inspect, correct
  references/
    install.md                   # OpenSCAD installation on Windows, macOS, Linux
    syntax.md                    # syntax cheat sheet
    patterns-2d.md               # profiles, rounded shapes, text, cross-sections
    patterns-3d.md               # shells, holes, fits, brackets, cutaway views
    libraries.md                 # BOSL2, NopSCADlib, Round-Anything, threads
    render-views.md              # headless rendering and camera syntax
    pitfalls.md                  # common traps
  scripts/
    render_views.py              # render top/front/side/iso views (stdlib only)
    check_stl.py                 # closed mesh, bounding box, volume (stdlib only)
  examples/
    block-with-spherical-cut.scad
```

## Install in OpenClaw

Add the **repository root** to `skills.load.extraDirs` (it contains the skill folder):

```
openclaw config set skills.load.extraDirs '["~/github_repos/openclaw-agent-standard","~/github_repos/sprintcx-openclaw-skills","~/github_repos/openscad-agent-skill"]' --strict-json
openclaw config validate
```

Keep your existing entries; only append the new one.

## Install in Hermes

```
hermes skills install https://raw.githubusercontent.com/sprintberlin/openscad-agent-skill/main/openscad-agent-skill/SKILL.md
```

Or clone the repo and add it to `skills.external_dirs` in `~/.hermes/config.yaml`.

## Requirements

- OpenSCAD (see `openscad-agent-skill/references/install.md`)
- Python 3 for the helper scripts (optional; the loop also works with plain CLI commands)
- An agent that can view images for the verification step

## Status

Early version. Scripts and rendering verified on Windows with OpenSCAD 2021.01 and Python 3.13. Linux and macOS not yet verified.

## License

MIT
