from django.db import models

# Create your models here.
class Cliente(models.Model):
    idcliente = models.IntegerField(db_column='IdCliente', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    dv = models.TextField(db_column='DV', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    idpais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='IdPais',related_name='paises')  # Field name made lowercase.
    iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='IdDepartamento',related_name='departamentos')  # Field name made lowercase.
    idmunicipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='IdMunicipio',related_name='municipios')  # Field name made lowercase.
    idsistema = models.ForeignKey('Sistema', models.DO_NOTHING, db_column='IdSistema',related_name='sistemas')  # Field name made lowercase.
    idtipodoc = models.ForeignKey('TipoDoc', models.DO_NOTHING, db_column='IdTipoDoc',related_name='tipodoc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre


class Sistema(models.Model):
    idsistema = models.IntegerField(db_column='idSistema', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sistema'
        verbose_name_plural = "Sistemas"

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    idestado = models.AutoField(db_column='IdEstado', primary_key=True)  # Field name made lowercase.
    tarea = models.CharField(db_column='Tarea', max_length=45, blank=True, null=True)  # Field name made lowercase.
    historiausuario = models.CharField(db_column='HistoriaUsuario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    errordetalle = models.TextField(db_column='ErrorDetalle', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    idbot = models.IntegerField(db_column='IdBot', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado'

class Pais(models.Model):
    idpais = models.IntegerField(db_column='IdPais', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    homologacion = models.TextField(db_column='Homologacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pais'
        verbose_name_plural = "Paises"

    def __str__(self):
        return self.descripcion

class TipoDoc(models.Model):
    idtipodoc = models.IntegerField(db_column='IdTipoDoc', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    homologacion = models.TextField(db_column='Homologacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_doc'
        verbose_name_plural = "Tipo de documento"

    def __str__(self):
        return self.descripcion


class Departamento(models.Model):
    iddepartamento = models.IntegerField(db_column='IdDepartamento', primary_key=True)  # Field name made lowercase.
    nombredepartamento = models.TextField(db_column='NombreDepartamento', blank=True, null=True)  # Field name made lowercase.
    homologacion = models.TextField(db_column='Homologacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.nombredepartamento


class Municipio(models.Model):
    idmunicipio = models.IntegerField(db_column='IdMunicipio', primary_key=True)  # Field name made lowercase. The composite primary key (IdMunicipio, IdDepartamento) found, that is not supported. The first column is selected.
    nombremunicipio = models.TextField(db_column='NombreMunicipio', blank=True, null=True)  # Field name made lowercase.
    homologacion = models.TextField(db_column='Homologacion', blank=True, null=True)  # Field name made lowercase.
    iddepartamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='IdDepartamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'municipio'
        unique_together = (('idmunicipio', 'iddepartamento'),)
        verbose_name_plural = "Municipios"

    def __str__(self):
        return self.nombremunicipio

