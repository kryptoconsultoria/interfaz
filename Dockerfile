# ┌────────── Etapa 1: Construcción del frontend con Vite ──────────────────────────────┐
FROM node:18-slim AS frontend
WORKDIR /app/frontend

RUN npm config set strict-ssl false

COPY frontend/package.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build

# ┌────────── Etapa 2: Backend Django ──────────────────────────────┐
FROM python:3.12 AS backend

# Dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia todo el proyecto
COPY . .

# Copia estáticos generados desde el frontend
COPY --from=frontend /app/frontend/dist /app/static/

# Copiar .env para que esté disponible
COPY .env .

# Instalar dependencias de Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Dar permisos al entrypoint
RUN chmod +x entrypoint.sh

# Exponer puerto (8000 en vez de 21, porque 21 es de FTP)
EXPOSE 8000

# Definir punto de entrada
ENTRYPOINT ["./entrypoint.sh"]
