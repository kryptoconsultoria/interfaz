# ┌────────── Etapa 1: Construcción del frontend con Vite ──────────────────────────────┐
FROM node:18-slim AS frontend
WORKDIR /app

# 1. Copiar solo package.json para evitar lockfiles no compatibles
COPY package.json ./

# 2. Instalar dependencias y asegura el binario nativo Linux
RUN npm install

# 3. Copia el resto del frontend y construye
COPY . .
RUN npm run build

EXPOSE 5173
CMD ["npm", "run", "dev:docker"]
