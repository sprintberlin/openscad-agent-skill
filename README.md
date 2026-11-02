# openscad-agent-skill

OpenSCAD 2D/3D modeling and verification for AI agents.

- `openscad-agent-skill/SKILL.md`: workflow
- `openscad-agent-skill/references/`: syntax, modeling patterns and installation
- `openscad-agent-skill/scripts/check_stl.py`: optional STL check
- `openscad-agent-skill/examples/`: example model

## OpenClaw

Clone this repository and add its root to `skills.load.extraDirs`, preserving existing entries. See [OpenClaw skills configuration](https://docs.openclaw.ai/tools/skills).

## Hermes

```sh
hermes skills install https://raw.githubusercontent.com/sprintberlin/openscad-agent-skill/main/openscad-agent-skill/SKILL.md
```

Alternatively, clone the repository and add its root to `skills.external_dirs` in `~/.hermes/config.yaml`.

## Requirements

OpenSCAD and an image viewer; Python 3 for the optional STL check.

## License

MIT
