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
export JWT_SECRET_KEY='fb25196e792c5d0a48206fd61e54e71aaf1e6e8c364af84581031e103c927945'
export TOKEN_ALGORITHM='HS256'
export ACCESS_TOKEN_EXPIRE_MINUTES='60'

cd "$repo_root/apps/api"
uv run alembic upgrade head
uv run python -m pytest "$@"
