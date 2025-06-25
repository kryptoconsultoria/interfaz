# ┌────────── Etapa 1: Construcción del frontend con Vite ──────────────────────────────┐
FROM node:18-slim AS frontend
WORKDIR /app/frontend

COPY frontend/package.json frontend/package-lock.json ./
RUN npm install


COPY frontend/ ./
RUN npm run build

# ┌────────── Etapa 2: Backend Django ──────────────────────────────┐
FROM python:3.12 AS backend

RUN apt-get update && apt-get install -y \
    build-essential libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiara todo menos lo que se ignora en .dockerignore
COPY . .

# Instalar dependencias de Python
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY --from=frontend /app/static /app/static

# Ejecutar collectstatic
RUN python manage.py collectstatic --noinput

# Exponer puerto
EXPOSE 21

# Comando de arranque
CMD ["python", "manage.py", "runserver", "0.0.0.0:21"]




