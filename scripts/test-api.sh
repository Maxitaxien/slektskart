#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
compose_file="$repo_root/compose.test.yaml"

cleanup() {
    docker compose --progress quiet -f "$compose_file" down -v
}

trap cleanup EXIT

docker compose --progress quiet -f "$compose_file" up -d --wait

export DATABASE_URL='postgresql+psycopg://test_user:test_password@localhost:5433/slektskart_test'

cd "$repo_root/apps/api"
uv run alembic upgrade head
uv run python -m pytest "$@"
