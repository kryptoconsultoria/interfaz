#!/bin/bash
set -e

echo "📄 Cargando variables desde .env"
[ -f .env ] && export $(grep -v '^#' .env | xargs)

echo "🛠 Ejecutando makemigrations"
python manage.py makemigrations --noinput

echo "🧱 Ejecutando migrate"
python manage.py migrate --noinput

echo "📦 Ejecutando collectstatic"
python manage.py collectstatic --noinput

echo "🚀 Iniciando servidor Django"
exec python manage.py runserver 0.0.0.0:21