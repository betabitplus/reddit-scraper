#!/usr/bin/env bash

py_lib_project_config_python() {
  if [ -n "${VIRTUAL_ENV:-}" ] && [ -x "$VIRTUAL_ENV/bin/python" ]; then
    printf '%s\n' "$VIRTUAL_ENV/bin/python"
    return 0
  fi

  if [ -x ".venv/bin/python" ]; then
    printf '%s\n' ".venv/bin/python"
    return 0
  fi

  if command -v python3 >/dev/null 2>&1; then
    printf '%s\n' "python3"
    return 0
  fi

  if command -v python >/dev/null 2>&1; then
    printf '%s\n' "python"
    return 0
  fi

  return 1
}

py_lib_read_project_env_config() {
  local repo_root="$1"
  local python_bin
  python_bin="$(py_lib_project_config_python)" || return 1

  "$python_bin" - "$repo_root/pyproject.toml" <<'PY'
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

pyproject_path = Path(sys.argv[1])
with pyproject_path.open("rb") as pyproject_file:
    pyproject = tomllib.load(pyproject_file)

tooling = pyproject["tool"]["py_lib_starter"]
env_prefix = tooling["env_prefix"].strip()

if not re.fullmatch(r"[A-Z][A-Z0-9_]*", env_prefix):
    msg = "[tool.py_lib_starter].env_prefix must be an uppercase env-var prefix."
    raise SystemExit(msg)

print(env_prefix)
PY
}

py_lib_load_project_env_config() {
  local repo_root="${1:-$(pwd)}"
  local config_lines
  mapfile -t config_lines < <(py_lib_read_project_env_config "$repo_root") || return 1

  if [ "${#config_lines[@]}" -ne 1 ]; then
    return 1
  fi

  PY_LIB_PROJECT_ENV_PREFIX="${config_lines[0]}"

  export PY_LIB_PROJECT_ENV_PREFIX
}

py_lib_expand_env_file_path() {
  local env_file_path="$1"

  case "$env_file_path" in
    \~)
      printf '%s\n' "$HOME"
      ;;
    \~/*)
      printf '%s/%s\n' "$HOME" "${env_file_path#"~/"}"
      ;;
    \$HOME*)
      printf '%s%s\n' "$HOME" "${env_file_path#\$HOME}"
      ;;
    \$\{HOME\}*)
      printf '%s%s\n' "$HOME" "${env_file_path#\$\{HOME\}}"
      ;;
    *)
      printf '%s\n' "$env_file_path"
      ;;
  esac
}

py_lib_find_betabit_secrets_root() {
  local repo_root="${1:-$(pwd)}"
  local candidate

  if [ -n "${BETABIT_SECRETS_ROOT:-}" ]; then
    candidate="$(py_lib_expand_env_file_path "$BETABIT_SECRETS_ROOT")"
    if [ -d "$candidate" ]; then
      printf '%s\n' "$candidate"
      return 0
    fi
    printf 'BETABIT_SECRETS_ROOT does not exist: %s\n' "$candidate" >&2
    return 1
  fi

  candidate="${repo_root%/}/../betabit-secrets"
  if [ -d "$candidate" ]; then
    (cd "$candidate" && pwd)
    return 0
  fi

  return 1
}

py_lib_dotenv_sops_if_exists() {
  local env_file="$1"
  local local_age_key_file="${HOME}/.config/sops/age/keys.txt"

  if [ ! -f "$env_file" ]; then
    return 0
  fi
  if ! command -v sops >/dev/null 2>&1; then
    printf 'Encrypted env file exists but sops is missing: %s\n' "$env_file" >&2
    return 1
  fi

  if [ -z "${SOPS_AGE_KEY_FILE:-}" ] && [ -f "$local_age_key_file" ]; then
    eval "$(SOPS_AGE_KEY_FILE="$local_age_key_file" sops decrypt "$env_file" | direnv dotenv bash /dev/stdin)"
  else
    eval "$(sops decrypt "$env_file" | direnv dotenv bash /dev/stdin)"
  fi
}

py_lib_load_browser_automation_proxy_env() {
  local repo_root="${1:-$(pwd)}"
  local secrets_root

  secrets_root="$(py_lib_find_betabit_secrets_root "$repo_root")" || return 0

  py_lib_dotenv_sops_if_exists "$secrets_root/browser-automation/proxy.sops.env"
}
