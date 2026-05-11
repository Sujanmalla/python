## Repo snapshot

- Project root: top-level Python scripts in the folder `C:\Users\acer\OneDrive\Desktop\Python1`
- Minimal, script-style repo: no build system, no tests, no CI detected.

## Purpose for an AI coding agent

Provide small, safe edits to simple Python scripts (examples, utilities, small CLI tools). Prefer minimal, well-tested changes and avoid large refactors — this repo appears educational/demo-focused.

## Key files and patterns

- `filehandling.py`: demonstrates basic file I/O (write/read/append/delete). Changes here should preserve simple, sequential behavior and avoid deleting user files unless the user explicitly asks.
- `Untitled-1.py`: an interactive hello/name/age script — keep stdin interactions intact when modifying; add non-interactive entry points (CLI args) only if requested.
- `README.md`: tiny project readme. Use it as the canonical place to add usage notes when you change run behavior.

## How to run (developer workflow)

All commands assume PowerShell on Windows and the workspace root as the current working directory.

Run a script directly with Python:

    python .\filehandling.py
    python .\Untitled-1.py

If you change a script and want to test non-interactively, prefer passing arguments instead of relying on input() so automated runs are simple.

Check git status and remote before pushing changes:

    git status
    git remote -v

Commit and push changes (HTTPS or SSH depending on repo config):

    git add <files>
    git commit -m "Describe change"
    git push -u origin main

## Project-specific conventions

- Files are simple, top-level Python scripts. Aim for small, focused edits and include a short usage comment at the top when adding CLI behavior.
- Avoid creating complex package layouts (no setup.py, no pyproject.toml present). If you introduce packages, update the README with run instructions.
- Be conservative with changes that touch the filesystem: `filehandling.py` demonstrates file deletion — do not run destructive operations on the user's machine without explicit confirmation.

## Integration points & external dependencies

- No external dependencies or services detected. No virtualenv/venv or dependency manifest present. If you add third-party packages, include a `requirements.txt` and mention how to install (pip install -r requirements.txt).

## Examples for common agent tasks

- To add a non-interactive runner for `Untitled-1.py`, add `if __name__ == '__main__'` and allow `--name`/`--age` CLI flags; keep original input() as fallback.
- To extend `filehandling.py` with a safe preview mode, add a `--dry-run` or `--show-file` flag that prints what would be deleted instead of performing deletion.

## What not to do

- Don't perform large automatic refactors across files (this repo lacks tests and CI).
- Don't delete or overwrite user files in the workspace unless the user explicitly instructs you to do so.

## When you need more info

- Ask the user for their intended behavior before making changes that alter file I/O or CLI semantics.
- If you add dependencies or a test framework, update `README.md` with setup and test commands.

---
If anything important is missing (CI, test commands, intended target Python version, or preferred auth method for git pushes), tell me what to ask the user and I will update this file.
