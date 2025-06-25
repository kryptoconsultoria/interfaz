#!/bin/bash
set -e

echo "🔧 Cargando variables de entorno"
[ -f .env ] && export $(cat .env | xargs)

echo "🛠 Aplicando migraciones..."
python manage.py migrate --database=admin_db panel_principal