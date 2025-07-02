# ┌────────── Etapa 1: Construcción del frontend con Vite ──────────────────────────────┐
FROM node:18-slim AS frontend
WORKDIR /app/frontend

# Desactivar validación SSL (SELF_SIGNED_CERT_IN_CHAIN)
RUN npm config set strict-ssl false

# 1. Copiar solo package.json para evitar lockfiles no compatibles
COPY frontend/package.json ./

# 2. Instalar dependencias y asegura el binario nativo Linux
RUN npm install

# 3. Copia el resto del frontend y construye
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

# Migraciones (aún pueden requerir BUILD VAR)
ARG DATABASE_URL_DEFAULT
ARG DATABASE_URL_MEDIOS
ARG DATABASE_URL_ADMIN
ENV DATABASE_URL_DEFAULT=${DATABASE_URL_DEFAULT} \
    DATABASE_URL_MEDIOS=${DATABASE_URL_MEDIOS} \
    DATABASE_URL_ADMIN=${DATABASE_URL_ADMIN}


# Variables de runtime
ENV ALLOWED_ORIGINS=${ALLOWED_ORIGINS} \
    CLIENT_ID=${CLIENT_ID} \
    CLIENT_SECRET=${CLIENT_SECRET} \
    DEBUG=${DEBUG:-False} \
    DOMAIN=${DOMAIN} \
    FASTAPI_URL=${FASTAPI_URL} \
    REFRESH_TOKEN=${REFRESH_TOKEN} \
    SECRET_KEY=${SECRET_KEY} \
    SITE_NAME=${SITE_NAME} \
    TENANT_ID=${TENANT_ID}

#Crear superusuario usando createsuperuser en una RUN separada
#RUN python manage.py createsuperuser --no-input \
#    --username "$DJANGO_SUPERUSER_USERNAME" \
#   --email "$DJANGO_SUPERUSER_EMAIL" || true

# collect static
RUN python manage.py collectstatic --noinput

# Migraciones iniciales admin
#RUN python manage.py migrate --database=admin_db && \
#    python manage.py migrate panel_principal --database=admin_db

# Ejecutar migraciones en runtime (si lo prefieres aquí)
#RUN python manage.py migrate --noinput

# Exponer puerto
EXPOSE 23

# Comando de arranque
CMD ["python", "manage.py", "runserver", "0.0.0.0:23"]