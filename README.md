# BuEditor

Standalone BuLang editor.

`BuEditor` is the editor for BuLang projects.

It exists as a separate project so it can evolve on its own and be used with different runtimes such as `bugl`, `bugame`, or `buogre`, without dragging the full engine build graph behind it.

The editor is meant for:
- editing `.bu` scripts
- running and compiling scripts with a configurable runtime
- growing a shared UI/tooling layer that is not tied to a single engine

Project layout:
- `src/` editor source code
- `vendor/` third-party dependencies used by the editor
- `config/` editor settings
- `workspaces/` workspace examples and presets
- `widgets/` shared editor widgets and notes

Build:

```bash
cmake -S . -B build
cmake --build build --target BuEditor -j4
```

Run:

```bash
./bin/bueditor
```

Configuration:
- `config/settings.json` stores editor defaults and runtime configuration
- `workspaces/` is where project-specific workspace files can live

Current direction:
- keep the editor decoupled from engine repos
- keep runtime/backend selection configurable
- consolidate widgets, panels, and tooling here
