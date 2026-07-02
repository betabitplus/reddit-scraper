# Setup

Use this file to provision a local contributor environment. For day-to-day
workflow, tests, hooks, and release conventions, use
[CONTRIBUTING.md](CONTRIBUTING.md).

## Prerequisites

- Python 3.13+
- `uv` installed
- optional `sops` and `age` for browser automation proxy env loading

Some e2e and workbench flows use `HTTP_PROXY` or `HTTPS_PROXY`. `.envrc` loads
them from this SOPS file when present:

- `../betabit-secrets/browser-automation/proxy.sops.env`

Set `BETABIT_SECRETS_ROOT` to use a different local path.

Edit it with SOPS:

```bash
sops ../betabit-secrets/browser-automation/proxy.sops.env
```

## First-Time Setup

Run this from the repository root:

```bash
bash scripts/env/setup.sh
direnv allow
bash scripts/env/doctor.sh
```

`scripts/env/setup.sh` runs `uv sync --group dev` and installs configured git
hook types. `direnv allow` lets `.envrc` activate the local environment.
`scripts/env/doctor.sh` checks common local setup problems.

To install or refresh all configured hook stages directly, run:

```bash
uv run pre-commit install
```

## Running Through Direnv

If a shell has not loaded `.envrc`, run repo commands through `direnv exec .`:

```bash
direnv exec . uv run pytest tests/reddit_scraper -m hermetic -q
direnv exec . uv run py-lib-smoke-public-api
```

## Devcontainer

The devcontainer provisions an in-container `.venv` with `uv sync --group dev`.
VS Code points to `${workspaceFolder}/.venv/bin/python` inside the container.

If VS Code loses the interpreter, run `Python: Clear Workspace Interpreter Setting`
and reselect `reddit-scraper (.venv)`.

## Clean Rebuild With Uv

```bash
rm -rf .venv
rm -f uv.lock
uv cache clean
uv cache prune
uv lock
uv sync --group dev
```
