# ┌────────── Etapa 1: Construcción del frontend con Vite ──────────────────────────────┐
FROM node:18-slim AS frontend
WORKDIR /app

# Desactivar validación SSL (SELF_SIGNED_CERT_IN_CHAIN)
RUN npm config set strict-ssl false

# 1. Copiar solo package.json para evitar lockfiles no compatibles
COPY frontend/package.json ./

# 2. Instalar dependencias y asegura el binario nativo Linux
RUN npm install

# 3. Copia el resto del frontend y construye
COPY frontend/ .
RUN npm run build

EXPOSE 5173
CMD ["npm", "run", "dev:docker"]
