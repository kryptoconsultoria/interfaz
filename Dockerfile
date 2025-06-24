# Etapa 1: Construcción del frontend con Vite
FROM node:18 AS frontend

WORKDIR /app/frontend


COPY frontend/package*.json ./
RUN npm install

COPY frontend/ .
RUN npm run build



# Etapa 2: Backend Django
FROM python:3.12 AS backend

RUN apt-get update && apt-get install -y \
    build-essential libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiara todo menos lo que se ignora en .dockerignore
COPY ..

# Instalar dependencias de Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar assets generados por Vite al lugar esperado por Django
COPY --from=frontend /app/frontend/dist ./static/

# Exponer puerto
EXPOSE 8000

# Comando de arranque
CMD ["gunicorn", "django_vite.wsgi:application", "--bind", "0.0.0.0:8000"]











