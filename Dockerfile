FROM python:3.12 AS builder

WORKDIR /app


# Instala herramientas de compilación necesarias
COPY requirements.txt .

# Asegura que haya versión moderna de wheel (para evitar errores con thriftpy2)
RUN pip install --upgrade pip wheel setuptools \
    && pip install --no-cache-dir -r requirements.txt

# ┌────────── Etapa final ──────────────────────────────┐
FROM python:3.12

WORKDIR /app

# Instala solo runtime dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Comando de arranque (ajusta según tu app)
CMD ["python", "manage.py", "runserver", "0.0.0.0:23"]











