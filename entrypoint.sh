#!/bin/bash
set -e

echo "Cargando entorno desde .env"
[ -f .env ] && export $(cat .env | xargs)

echo "Ejecutando migraciones..."
python manage.py migrate --database=admin_db panel_principal