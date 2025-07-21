from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Países"

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='ciudades')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'pais'], name='unique_ciudad_pais')
        ]
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return f"{self.nombre}, {self.pais.nombre}"

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True, related_name='empresas')
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True, blank=True, related_name='empresas')
    # Otros campos relevantes

    def __str__(self):
        return self.nombre

class Automatizacion(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        permissions = [
            ("puede_correr_automatizacion", "Puede correr automatización"),
        ]
    def __str__(self):
        return self.nombre

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True, related_name='perfiles')
    automatizaciones = models.ManyToManyField(Automatizacion, blank=True, related_name='usuarios')
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True, related_name='perfiles')
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True, blank=True, related_name='perfiles')

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

    def tiene_acceso_a(self, automatizacion_nombre):
        return self.automatizaciones.filter(nombre=automatizacion_nombre).exists()
