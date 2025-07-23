# admin.py
from django.contrib import admin
from .models import (PerfilUsuario,Automatizacion,Pais,Ciudad)


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

@admin.register(Ciudad)
class CiudadAdmin(AllFieldsAdmin): pass

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(AllFieldsAdmin): pass

@admin.register(Automatizacion)
class AutomatizacionAdmin(AllFieldsAdmin): pass
