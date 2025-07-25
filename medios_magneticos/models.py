# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bancos(models.Model):
    numid = models.CharField(db_column='NumId', max_length=15)  # Field name made lowercase.
    dv = models.CharField(max_length=3, blank=True, null=True)
    razonsocial = models.CharField(db_column='RazonSocial', max_length=45, blank=True, null=True)  # Field name made lowercase.
    coddpto = models.CharField(db_column='CodDpto', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codmcp = models.CharField(db_column='CodMcp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cuentas = models.TextField(db_column='Cuentas', blank=True, null=True)  # Field name made lowercase.
    idcliente = models.OneToOneField('Cliente', models.DO_NOTHING, db_column='IdCliente', primary_key=True)  # Field name made lowercase. The composite primary key (IdCliente, NumId) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'bancos'
        unique_together = (('idcliente', 'numid'),)

    def __str__(self):
        return self.razonsocial


class Cliente(models.Model):
    idcliente = models.IntegerField(db_column='IdCliente', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    dv = models.TextField(db_column='DV', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    idpais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='IdPais')  # Field name made lowercase.
    iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='IdDepartamento',related_name='departamentos')  # Field name made lowercase.
    idmunicipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='IdMunicipio',related_name='municipios')  # Field name made lowercase.
    idsistema = models.ForeignKey('Sistema', models.DO_NOTHING, db_column='IdSistema',related_name='sistemas')  # Field name made lowercase.
    idtipodoc = models.ForeignKey('TipoDoc', models.DO_NOTHING, db_column='IdTipoDoc',related_name='tipodocs')  # Field name made lowercase.
    idtipoinformante = models.IntegerField(db_column='IdTipoInformante')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nombre}"



class Columnas(models.Model):
    idcolumna = models.IntegerField(db_column='IdColumna', primary_key=True)  # Field name made lowercase.
    idformato = models.ForeignKey('Formato', models.DO_NOTHING, db_column='IdFormato', blank=True, null=True)  # Field name made lowercase.
    nombrecolumnabd = models.TextField(db_column='NombreColumnaBD', blank=True, null=True)  # Field name made lowercase.
    nombrecolumnadian = models.TextField(db_column='NombreColumnaDian', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'columnas'
        verbose_name_plural = "Columnas"

    def __str__(self):
        return self.nombrecolumnadian


class Concepto(models.Model):
    idconcepto = models.IntegerField(db_column='IdConcepto', primary_key=True)  # Field name made lowercase.
    idformato = models.ForeignKey('Formato', models.DO_NOTHING, db_column='IdFormato', blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'concepto'
        verbose_name_plural = "Conceptos"

    def __str__(self):
        return self.concepto


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


class Direccion(models.Model):
    abreviatura = models.CharField(db_column='Abreviatura', max_length=3, blank=True, null=True)  # Field name made lowercase.
    significado = models.CharField(db_column='Significado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    homologacion = models.TextField(db_column='Homologacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'direccion'
        verbose_name_plural = "Direcciones"

    def __str__(self):
        return self.significado


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
        verbose_name_plural = "Estados"


class Formato(models.Model):
    idformato = models.IntegerField(db_column='IdFormato', primary_key=True)  # Field name made lowercase.
    formato = models.CharField(db_column='Formato', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cuantiasmenores = models.IntegerField(db_column='CuantiasMenores', blank=True, null=True)  # Field name made lowercase.
    idformula = models.IntegerField(db_column='IdFormula', blank=True, null=True)  # Field name made lowercase.
    nombregral = models.CharField(db_column='NombreGral', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato'
        verbose_name_plural = "Formatos"

    def __str__(self):
        return self.formato



class Formulas(models.Model):
    idformula = models.IntegerField(db_column='IdFormula', primary_key=True)  # Field name made lowercase.
    formula = models.TextField(db_column='Formula', blank=True, null=True)  # Field name made lowercase.
    valor = models.TextField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formulas'
        verbose_name_plural = "Formulas"

    def __str__(self):
        return self.formula


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


class Puc(models.Model):
    idpuc = models.AutoField(db_column='IdPuc', primary_key=True)  # Field name made lowercase.
    cuentacontable = models.CharField(db_column='CuentaContable', max_length=255, db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    formato = models.TextField(db_column='Formato', blank=True, null=True)  # Field name made lowercase.
    concepto = models.TextField(db_column='Concepto', blank=True, null=True)  # Field name made lowercase.
    columna = models.TextField(db_column='Columna', blank=True, null=True)  # Field name made lowercase.
    idformula = models.ForeignKey(Formulas, models.DO_NOTHING, db_column='IdFormula')  # Field name made lowercase.
    nitreporta = models.TextField(db_column='NitReporta', blank=True, null=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='IdCliente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'puc'


class Sistema(models.Model):
    idsistema = models.IntegerField(db_column='idSistema', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sistema'

    def __str__(self):
        return self.nombre


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

class TipoInformante(models.Model):
    idtipoinformate = models.IntegerField(db_column='IdTipoInformate', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_informante'
        verbose_name_plural = "Tipo de informante"

    def __str__(self):
        return self.descripcion

class ExclusionNits(models.Model):
    idexclusionnits = models.AutoField(db_column='IdExclusionNits', primary_key=True)  # Field name made lowercase.
    idtercero = models.CharField(db_column='IdTercero', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idtipodoc = models.ForeignKey('TipoDoc', models.DO_NOTHING, db_column='IdTipoDoc')  # Field name made lowercase.
    idformato = models.ForeignKey('Formato', models.DO_NOTHING, db_column='IdFormato')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exclusion_nits'
        verbose_name_plural = "Exclusión de nits"
