secrets_root="${BETABIT_SECRETS_ROOT:-}"
if [ -z "$secrets_root" ]; then
  secrets_root="$PWD/../betabit-secrets"
fi

case "$secrets_root" in
  \~) secrets_root="$HOME" ;;
  \~/*) secrets_root="$HOME/${secrets_root#"~/"}" ;;
esac

proxy_env="$secrets_root/browser-automation/proxy.sops.env"
if [ -f "$proxy_env" ]; then
  if ! command -v sops >/dev/null 2>&1; then
    printf '%s\n' "Found $proxy_env, but sops is not installed." >&2
    return 1
  fi

  age_key_file="$HOME/.config/sops/age/keys.txt"
  if [ -z "${SOPS_AGE_KEY_FILE:-}" ] && [ -f "$age_key_file" ]; then
    eval "$(SOPS_AGE_KEY_FILE="$age_key_file" sops decrypt "$proxy_env" | direnv dotenv bash /dev/stdin)"
  else
    eval "$(sops decrypt "$proxy_env" | direnv dotenv bash /dev/stdin)"
  fi
fi
