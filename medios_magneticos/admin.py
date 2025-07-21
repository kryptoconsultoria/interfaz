# admin.py

from django.contrib import admin
from .models import (
    Pais,
    Cliente,
    Columnas,
    Concepto,
    Departamento,
    Direccion,
    ExclusionNits,
    Formato,
    Formulas,
    Municipio,
    TipoDoc,
    TipoInformante,
)

# Registro directo de una lista de modelos
admin.site.register([
    Pais,
    Cliente,
    Columnas,
    Concepto,
    Departamento,
    Direccion,
    ExclusionNits,
    Formato,
    Formulas,
    Municipio,
    TipoDoc,
    TipoInformante,
])
