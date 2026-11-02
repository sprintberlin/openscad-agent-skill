# openscad-agent-skill

A skill for AI agents (OpenClaw, Hermes, Claude Code and others that read `SKILL.md`) that teaches 2D and 3D modeling with OpenSCAD with one rule: **a model counts as done only after its rendered views were inspected.**

## Contents

- `SKILL.md`: the modeling, render and inspect loop
- `references/`: install, render views, modeling patterns, pitfalls
- `examples/`: parts that were rendered and inspected

## Install

Copy this folder into the skill directory of your agent, or install from the repository. No scripts are required; the agent only needs a shell and OpenSCAD.

## Status

Early version. Commands verified on Windows with OpenSCAD 2021.01. Linux and macOS not yet verified.

## License

MIT
