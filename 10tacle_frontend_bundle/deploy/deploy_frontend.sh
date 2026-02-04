#!/usr/bin/env bash
set -euo pipefail

ZIP_PATH="${1:-frontend.zip}"

if [[ ! -f "$ZIP_PATH" ]]; then
  echo "No encuentro $ZIP_PATH. Uso: $0 /ruta/a/frontend.zip"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

# Limpia y descomprime el build
rm -rf "$SCRIPT_DIR/reflex-frontend"
mkdir -p "$SCRIPT_DIR/reflex-frontend"
unzip -q "$ZIP_PATH" -d "$SCRIPT_DIR/reflex-frontend"

# Para y borra el contenedor/stack anterior
docker compose -f "$ROOT_DIR/docker-compose.yml" down --remove-orphans

# Arranca el contenedor con el frontend actualizado
docker compose -f "$ROOT_DIR/docker-compose.yml" up -d

echo "✅ Frontend desplegado. Nginx escuchando en :3000 dentro de la red 'proxy' como alias 10tacle_app."
echo "   Traefik seguirá enroutando 10tacle.org -> servicio '10tacle' -> http://10tacle_app:3000/ (sin tocar dynamic_conf.yml)."