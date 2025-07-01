#!/bin/bash
set -e

# Ejecutar collectstatic sólo si existe FASTAPI_URL (asume que otras vars están definidas)
echo "[Entrypoint] Ejecutando collectstatic..."
python manage.py collectstatic --noinput

#Migraciones inicales admin
python manage.py migrate --database=admin_db  && \
python manage.py migrate panel_principal --database=admin_db

# Ejecutar migraciones en runtime (si lo prefieres aquí)
echo "[Entrypoint] Aplicando migraciones..."
python manage.py migrate --noinput

# Ejecutar el comando principal
echo "[Entrypoint] Iniciando servidor: $@"
exec "$@"