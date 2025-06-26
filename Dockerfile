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


# 1. Definir argumentos de build para usuario, email y contraseña
ARG DJANGO_SUPERUSER_USERNAME=felipe
ARG DJANGO_SUPERUSER_EMAIL=felipe.castano@krypto.com.co
ARG DJANGO_SUPERUSER_PASSWORD=hola123

# 2. Pasar argumentos a variables de entorno en la imagen
ENV DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME \
    DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL \
    DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD

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

# migraciones iniciales
# RUN python manage.py migrate --database=admin_db panel_principal
RUN python manage.py migrate --database=admin_db  && \
    python manage.py migrate panel_principal --database=admin_db


#Crear superusuario usando createsuperuser en una RUN separada
RUN python manage.py createsuperuser --no-input \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL" || true

# Exponer puerto
EXPOSE 23

# Comando de arranque
CMD ["python", "manage.py", "runserver", "0.0.0.0:23"]