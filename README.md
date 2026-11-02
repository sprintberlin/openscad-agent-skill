# openscad-agent-skill

OpenSCAD 2D/3D modeling for AI agents. English, agent-neutral `SKILL.md`, direct OpenSCAD CLI commands, rendered-view verification.

## Files

- `openscad-agent-skill/SKILL.md`: modeling and verification workflow
- `references/`: install, syntax, 2D/3D patterns, libraries, pitfalls
- `scripts/check_stl.py`: optional STL check (closed mesh, bounding box, volume); Python 3 standard library
- `examples/`: tested starting points

## OpenClaw

Clone the repository, then append its root to `skills.load.extraDirs`. The root contains the skill folder.

```sh
openclaw config set skills.load.extraDirs '["~/github_repos/openclaw-agent-standard","~/github_repos/sprintcx-openclaw-skills","~/github_repos/openscad-agent-skill"]' --strict-json
openclaw config validate
```

Keep existing entries; only append the new path.

## Hermes

```sh
hermes skills install https://raw.githubusercontent.com/sprintberlin/openscad-agent-skill/main/openscad-agent-skill/SKILL.md
```

Or clone and add the repository to `skills.external_dirs` in `~/.hermes/config.yaml`.

## Requirements

- OpenSCAD on PATH
- Python 3 only for the optional STL check
- Image viewing for visual verification

## License

MIT
