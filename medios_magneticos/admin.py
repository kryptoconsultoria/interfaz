from django.contrib import admin
from .models import (
    Pais, Cliente, Columnas, Concepto, Departamento, Direccion,
    ExclusionNits, Formato, Formulas, Municipio, TipoDoc, TipoInformante,
)
class AllFieldsAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        campos = []
        for field in self.model._meta.fields:
            if field.many_to_one:
                campos.append(f"{field.name}_id")  # solo el número
            else:
                campos.append(field.name)
        return campos

@admin.register(Pais)
class PaisAdmin(AllFieldsAdmin): pass

@admin.register(Cliente)
class ClienteAdmin(AllFieldsAdmin): pass

@admin.register(Columnas)
class ColumnasAdmin(AllFieldsAdmin): pass

@admin.register(Concepto)
class ConceptoAdmin(AllFieldsAdmin): pass

@admin.register(Departamento)
class DepartamentoAdmin(AllFieldsAdmin): pass

@admin.register(Direccion)
class DireccionAdmin(AllFieldsAdmin): pass

@admin.register(ExclusionNits)
class ExclusionNitsAdmin(AllFieldsAdmin): pass

@admin.register(Formato)
class FormatoAdmin(AllFieldsAdmin): pass

@admin.register(Formulas)
class FormulasAdmin(AllFieldsAdmin): pass

@admin.register(Municipio)
class MunicipioAdmin(AllFieldsAdmin): pass

@admin.register(TipoDoc)
class TipoDocAdmin(AllFieldsAdmin): pass

@admin.register(TipoInformante)
class TipoInformanteAdmin(AllFieldsAdmin): pass