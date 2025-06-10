# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BalanceAliaddo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.TextField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.TextField(db_column='Cuenta', blank=True, null=True)  # Field name made lowercase.
    tercero = models.TextField(db_column='Tercero', blank=True, null=True)  # Field name made lowercase.
    identificacion = models.TextField(db_column='Identificacion', blank=True, null=True)  # Field name made lowercase.
    saldoinicial = models.TextField(db_column='SaldoInicial', blank=True, null=True)  # Field name made lowercase.
    debito = models.TextField(db_column='Debito', blank=True, null=True)  # Field name made lowercase.
    credito = models.TextField(db_column='Credito', blank=True, null=True)  # Field name made lowercase.
    saldofinal = models.TextField(db_column='SaldoFinal', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'balance_aliaddo'


class BalanceAllegra(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nivel = models.TextField(db_column='Nivel', blank=True, null=True)  # Field name made lowercase.
    codigo = models.TextField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    cuentacontable = models.TextField(db_column='CuentaContable', blank=True, null=True)  # Field name made lowercase.
    identificacion = models.TextField(db_column='Identificacion', blank=True, null=True)  # Field name made lowercase.
    nombredeltercero = models.TextField(db_column='NombreDelTercero', blank=True, null=True)  # Field name made lowercase.
    saldoanterior = models.TextField(db_column='SaldoAnterior', blank=True, null=True)  # Field name made lowercase.
    debito = models.TextField(db_column='Debito', blank=True, null=True)  # Field name made lowercase.
    credito = models.TextField(db_column='Credito', blank=True, null=True)  # Field name made lowercase.
    saldofinal = models.TextField(db_column='SaldoFinal', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'balance_allegra'


class BalanceAvansys(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.TextField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.TextField(db_column='Cuenta', blank=True, null=True)  # Field name made lowercase.
    referencia = models.TextField(db_column='Referencia', blank=True, null=True)  # Field name made lowercase.
    tercero = models.TextField(db_column='Tercero', blank=True, null=True)  # Field name made lowercase.
    saldoinicial = models.TextField(db_column='SaldoInicial', blank=True, null=True)  # Field name made lowercase.
    debito = models.TextField(db_column='Debito', blank=True, null=True)  # Field name made lowercase.
    credito = models.TextField(db_column='Credito', blank=True, null=True)  # Field name made lowercase.
    saldofinal = models.TextField(db_column='SaldoFinal', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'balance_avansys'


class BalanceSiigoNube(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nivel = models.TextField(db_column='Nivel', blank=True, null=True)  # Field name made lowercase.
    transaccional = models.TextField(db_column='Transaccional', blank=True, null=True)  # Field name made lowercase.
    codigocuentacontable = models.TextField(db_column='CodigoCuentaContable', blank=True, null=True)  # Field name made lowercase.
    nombrecuentacontable = models.TextField(db_column='NombreCuentaContable', blank=True, null=True)  # Field name made lowercase.
    identificacion = models.TextField(db_column='Identificacion', blank=True, null=True)  # Field name made lowercase.
    sucursal = models.TextField(db_column='Sucursal', blank=True, null=True)  # Field name made lowercase.
    nombretercero = models.TextField(db_column='NombreTercero', blank=True, null=True)  # Field name made lowercase.
    saldoinicial = models.TextField(db_column='SaldoInicial', blank=True, null=True)  # Field name made lowercase.
    debito = models.TextField(db_column='Debito', blank=True, null=True)  # Field name made lowercase.
    credito = models.TextField(db_column='Credito', blank=True, null=True)  # Field name made lowercase.
    saldofinal = models.TextField(db_column='SaldoFinal', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'balance_siigo_nube'


class BalanceSiigoPyme(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    grupo = models.TextField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.TextField(db_column='Cuenta', blank=True, null=True)  # Field name made lowercase.
    subcuenta = models.TextField(db_column='Subcuenta', blank=True, null=True)  # Field name made lowercase.
    auxiliar = models.TextField(db_column='Auxiliar', blank=True, null=True)  # Field name made lowercase.
    subauxil = models.TextField(db_column='Subauxil', blank=True, null=True)  # Field name made lowercase.
    nit = models.CharField(db_column='Nit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sucursal = models.TextField(db_column='Sucursal', blank=True, null=True)  # Field name made lowercase.
    digitoverificacion = models.TextField(db_column='DigitoVerificacion', blank=True, null=True)  # Field name made lowercase.
    centroc = models.TextField(db_column='CentroC', blank=True, null=True)  # Field name made lowercase.
    empty1 = models.TextField(db_column='Empty1', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    ultimomov = models.TextField(db_column='UltimoMov', blank=True, null=True)  # Field name made lowercase.
    saldoanterior = models.TextField(db_column='SaldoAnterior', blank=True, null=True)  # Field name made lowercase.
    debito = models.TextField(db_column='Debito', blank=True, null=True)  # Field name made lowercase.
    credito = models.TextField(db_column='Credito', blank=True, null=True)  # Field name made lowercase.
    nuevosaldo = models.TextField(db_column='NuevoSaldo', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'balance_siigo_pyme'


class BalanceTercerosSiigoNube(models.Model):
    cuentacontable = models.TextField(db_column='CuentaContable', blank=True, null=True)  # Field name made lowercase.
    detallecuenta = models.TextField(db_column='DetalleCuenta', blank=True, null=True)  # Field name made lowercase.
    vigencia = models.TextField(db_column='Vigencia', blank=True, null=True)  # Field name made lowercase.
    tipodedocumento = models.TextField(db_column='TipoDeDocumento', blank=True, null=True)  # Field name made lowercase.
    numerodedocumento = models.CharField(db_column='NumeroDeDocumento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    digitoverificaciondv = models.TextField(db_column='DigitoVerificacionDV', blank=True, null=True)  # Field name made lowercase.
    nombresapellidosrazonsocial = models.TextField(db_column='NombresApellidosRazonSocial', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    codigociudadomunicipio = models.TextField(db_column='CodigoCiudadOMunicipio', blank=True, null=True)  # Field name made lowercase.
    codigodepartamento = models.TextField(db_column='CodigoDepartamento', blank=True, null=True)  # Field name made lowercase.
    telefono = models.TextField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    correoelectronico = models.TextField(db_column='CorreoElectronico', blank=True, null=True)  # Field name made lowercase.
    tarifa = models.TextField(db_column='Tarifa', blank=True, null=True)  # Field name made lowercase.
    saldoinicial = models.TextField(db_column='SaldoInicial', blank=True, null=True)  # Field name made lowercase.
    debito = models.TextField(db_column='Debito', blank=True, null=True)  # Field name made lowercase.
    credito = models.TextField(db_column='Credito', blank=True, null=True)  # Field name made lowercase.
    saldofinal = models.TextField(db_column='SaldoFinal', blank=True, null=True)  # Field name made lowercase.
    codpais = models.TextField(db_column='CodPais', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'balance_terceros_siigo_nube'


class Balances(models.Model):
    idbalances = models.AutoField(db_column='IdBalances', primary_key=True)  # Field name made lowercase.
    entidadinformante = models.CharField(db_column='EntidadInformante', max_length=45, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=255, db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.TextField(db_column='TipoDoc', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    numid = models.TextField(db_column='NumId', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    dv = models.TextField(db_column='DV', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    coddpto = models.TextField(db_column='CodDpto', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    codmcp = models.TextField(db_column='CodMcp', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    departamento = models.TextField(db_column='Departamento', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    municipio = models.TextField(db_column='Municipio', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    paisresidencia = models.TextField(db_column='PaisResidencia', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.TextField(db_column='PrimerApellido', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.TextField(db_column='SegundoApellido', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    primernombre = models.TextField(db_column='PrimerNombre', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.TextField(db_column='OtrosNombres', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.TextField(db_column='RazonSocial', db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    saldoinicial = models.FloatField(db_column='SaldoInicial', blank=True, null=True)  # Field name made lowercase.
    debito = models.FloatField(db_column='Debito', blank=True, null=True)  # Field name made lowercase.
    credito = models.FloatField(db_column='Credito', blank=True, null=True)  # Field name made lowercase.
    saldofinal = models.FloatField(db_column='SaldoFinal', blank=True, null=True)  # Field name made lowercase.
    encontradodian = models.CharField(db_column='EncontradoDIAN', max_length=2, db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'balances'


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


class CiudadesSiigoNube(models.Model):
    pais = models.TextField(db_column='Pais', blank=True, null=True)  # Field name made lowercase.
    estadodepartamento = models.TextField(db_column='EstadoDepartamento', blank=True, null=True)  # Field name made lowercase.
    ciudad = models.TextField(db_column='Ciudad', blank=True, null=True)  # Field name made lowercase.
    codigopais = models.TextField(db_column='CodigoPais', blank=True, null=True)  # Field name made lowercase.
    codigoestadodepartamento = models.CharField(db_column='CodigoEstadoDepartamento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codigociudad = models.CharField(db_column='CodigoCiudad', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ciudades_siigo_nube'


class Cliente(models.Model):
    idcliente = models.IntegerField(db_column='IdCliente', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    dv = models.TextField(db_column='DV', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    idpais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='IdPais')  # Field name made lowercase.
    iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='IdDepartamento')  # Field name made lowercase.
    idmunicipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='IdMunicipio')  # Field name made lowercase.
    idsistema = models.ForeignKey('Sistema', models.DO_NOTHING, db_column='IdSistema')  # Field name made lowercase.
    idtipodoc = models.ForeignKey('TipoDoc', models.DO_NOTHING, db_column='IdTipoDoc')  # Field name made lowercase.
    idtipoinformante = models.IntegerField(db_column='IdTipoInformante')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class Columnas(models.Model):
    idcolumna = models.IntegerField(db_column='IdColumna', primary_key=True)  # Field name made lowercase.
    idformato = models.ForeignKey('Formato', models.DO_NOTHING, db_column='IdFormato', blank=True, null=True)  # Field name made lowercase.
    nombrecolumnabd = models.TextField(db_column='NombreColumnaBD', blank=True, null=True)  # Field name made lowercase.
    nombrecolumnadian = models.TextField(db_column='NombreColumnaDian', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'columnas'


class Concepto(models.Model):
    idconcepto = models.IntegerField(db_column='IdConcepto', primary_key=True)  # Field name made lowercase.
    idformato = models.ForeignKey('Formato', models.DO_NOTHING, db_column='IdFormato', blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'concepto'


class Departamento(models.Model):
    iddepartamento = models.IntegerField(db_column='IdDepartamento', primary_key=True)  # Field name made lowercase.
    nombredepartamento = models.TextField(db_column='NombreDepartamento', blank=True, null=True)  # Field name made lowercase.
    homologacion = models.TextField(db_column='Homologacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'


class Direccion(models.Model):
    abreviatura = models.CharField(db_column='Abreviatura', max_length=3, blank=True, null=True)  # Field name made lowercase.
    significado = models.CharField(db_column='Significado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    homologacion = models.TextField(db_column='Homologacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'direccion'


class Estado(models.Model):
    idestado = models.AutoField(db_column='IdEstado', primary_key=True)  # Field name made lowercase.
    tarea = models.CharField(db_column='Tarea', max_length=45, blank=True, null=True)  # Field name made lowercase.
    historiausuario = models.CharField(db_column='HistoriaUsuario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    errordetalle = models.TextField(db_column='ErrorDetalle', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    idbot = models.IntegerField(db_column='IdBot', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado'


class ExclusionNits(models.Model):
    idexclusionnits = models.AutoField(db_column='IdExclusionNits', primary_key=True)  # Field name made lowercase.
    idtercero = models.CharField(db_column='IdTercero', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idtipodoc = models.ForeignKey('TipoDoc', models.DO_NOTHING, db_column='IdTipoDoc')  # Field name made lowercase.
    idformato = models.ForeignKey('Formato', models.DO_NOTHING, db_column='IdFormato')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exclusion_nits'


class Formato(models.Model):
    idformato = models.IntegerField(db_column='IdFormato', primary_key=True)  # Field name made lowercase.
    formato = models.CharField(db_column='Formato', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cuantiasmenores = models.IntegerField(db_column='CuantiasMenores', blank=True, null=True)  # Field name made lowercase.
    idformula = models.IntegerField(db_column='IdFormula', blank=True, null=True)  # Field name made lowercase.
    nombregral = models.CharField(db_column='NombreGral', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato'


class Formato1001(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numid = models.CharField(db_column='NumId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.CharField(db_column='OtrosNombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coddpto = models.CharField(db_column='CodDpto', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codmcp = models.CharField(db_column='CodMcp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    paisresidencia = models.CharField(db_column='PaisResidencia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    pagodeducible = models.IntegerField(db_column='PagoDeducible', blank=True, null=True)  # Field name made lowercase.
    pagonodeducible = models.IntegerField(db_column='PagoNoDeducible', blank=True, null=True)  # Field name made lowercase.
    ivadeducible = models.IntegerField(db_column='IvaDeducible', blank=True, null=True)  # Field name made lowercase.
    ivanodeducible = models.IntegerField(db_column='IvaNoDeducible', blank=True, null=True)  # Field name made lowercase.
    retpractrenta = models.IntegerField(db_column='RetPractRenta', blank=True, null=True)  # Field name made lowercase.
    retasumrenta = models.IntegerField(db_column='RetAsumRenta', blank=True, null=True)  # Field name made lowercase.
    retpractivaresp = models.IntegerField(db_column='RetPractIvaResp', blank=True, null=True)  # Field name made lowercase.
    retpractivanores = models.IntegerField(db_column='RetPractIvaNoRes', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1001'


class Formato1001Cuantias(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numid = models.CharField(db_column='NumId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.CharField(db_column='OtrosNombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coddpto = models.CharField(db_column='CodDpto', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codmcp = models.CharField(db_column='CodMcp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    paisresidencia = models.CharField(db_column='PaisResidencia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    pagodeducible = models.BigIntegerField(db_column='PagoDeducible', blank=True, null=True)  # Field name made lowercase.
    pagonodeducible = models.BigIntegerField(db_column='PagoNoDeducible', blank=True, null=True)  # Field name made lowercase.
    ivadeducible = models.BigIntegerField(db_column='IvaDeducible', blank=True, null=True)  # Field name made lowercase.
    ivanodeducible = models.BigIntegerField(db_column='IvaNoDeducible', blank=True, null=True)  # Field name made lowercase.
    retpractrenta = models.BigIntegerField(db_column='RetPractRenta', blank=True, null=True)  # Field name made lowercase.
    retasumrenta = models.BigIntegerField(db_column='RetAsumRenta', blank=True, null=True)  # Field name made lowercase.
    retpractivaresp = models.BigIntegerField(db_column='RetPractIvaResp', blank=True, null=True)  # Field name made lowercase.
    retpractivanores = models.BigIntegerField(db_column='RetPractIvaNoRes', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1001_cuantias'


class Formato1003(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numid = models.CharField(db_column='NumId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.CharField(db_column='OtrosNombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coddpto = models.CharField(db_column='CodDpto', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codmcp = models.CharField(db_column='CodMcp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    valorpagoret = models.BigIntegerField(db_column='ValorPagoRet', blank=True, null=True)  # Field name made lowercase.
    retpract = models.BigIntegerField(db_column='RetPract', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1003'


class Formato1005(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numid = models.CharField(db_column='NumId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.CharField(db_column='OtrosNombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impuestodescontable = models.BigIntegerField(db_column='ImpuestoDescontable', blank=True, null=True)  # Field name made lowercase.
    ivadevolucionesventas = models.BigIntegerField(db_column='IVADevolucionesVentas', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1005'


class Formato1006(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numid = models.CharField(db_column='NumId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.CharField(db_column='OtrosNombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    impuestogenerado = models.BigIntegerField(db_column='ImpuestoGenerado', blank=True, null=True)  # Field name made lowercase.
    ivarecuperado = models.BigIntegerField(db_column='IVARecuperado', blank=True, null=True)  # Field name made lowercase.
    impuestoconsumo = models.BigIntegerField(db_column='ImpuestoConsumo', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1006'


class Formato1007(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numid = models.CharField(db_column='NumId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.CharField(db_column='OtrosNombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paisresidencia = models.CharField(db_column='PaisResidencia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ingresosbrutos = models.BigIntegerField(db_column='IngresosBrutos', blank=True, null=True)  # Field name made lowercase.
    devolucionesrebajasdescuentos = models.BigIntegerField(db_column='DevolucionesRebajasDescuentos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1007'


class Formato1008(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numid = models.CharField(db_column='NumId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.CharField(db_column='OtrosNombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coddpto = models.CharField(db_column='CodDpto', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codmcp = models.CharField(db_column='CodMcp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    paisresidencia = models.CharField(db_column='PaisResidencia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    saldoctascobrar = models.BigIntegerField(db_column='SaldoCtasCobrar', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1008'


class Formato1008Cuantias(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numid = models.CharField(db_column='NumId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.CharField(db_column='OtrosNombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coddpto = models.CharField(db_column='CodDpto', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codmcp = models.CharField(db_column='CodMcp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    paisresidencia = models.CharField(db_column='PaisResidencia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    saldoctascobrar = models.BigIntegerField(db_column='SaldoCtasCobrar', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1008_cuantias'


class Formato1009(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numid = models.CharField(db_column='NumId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.CharField(db_column='OtrosNombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coddpto = models.CharField(db_column='CodDpto', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codmcp = models.CharField(db_column='CodMcp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    paisresidencia = models.CharField(db_column='PaisResidencia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    saldoctaspagar = models.BigIntegerField(db_column='SaldoCtasPagar', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1009'


class Formato1009Cuantias(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numid = models.CharField(db_column='NumId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.CharField(db_column='OtrosNombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coddpto = models.CharField(db_column='CodDpto', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codmcp = models.CharField(db_column='CodMcp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    paisresidencia = models.CharField(db_column='PaisResidencia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    saldoctaspagar = models.BigIntegerField(db_column='SaldoCtasPagar', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1009_cuantias'


class Formato1010(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numidsocio = models.CharField(db_column='NumIdSocio', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    primerapellidosocio = models.CharField(db_column='PrimerApellidoSocio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellidosocio = models.CharField(db_column='SegundoApellidoSocio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombresocio = models.CharField(db_column='PrimerNombreSocio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombressocio = models.CharField(db_column='OtrosNombresSocio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coddpto = models.CharField(db_column='CodDpto', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codmcp = models.CharField(db_column='CodMcp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    paisresidencia = models.CharField(db_column='PaisResidencia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    valorpatacciones = models.CharField(db_column='ValorPatAcciones', max_length=50, blank=True, null=True)  # Field name made lowercase.
    porcentajeparticipacion = models.CharField(db_column='PorcentajeParticipacion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    porcentajeparticipaciondecimal = models.CharField(db_column='PorcentajeParticipacionDecimal', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1010'


class Formato1011(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    saldo = models.BigIntegerField(db_column='Saldo', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1011'


class Formato1012(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numid = models.CharField(db_column='NumId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.CharField(db_column='OtrosNombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paisresidencia = models.CharField(db_column='PaisResidencia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    valoral3112 = models.BigIntegerField(db_column='ValorAl3112', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1012'


class Formato1647(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    concepto = models.TextField(db_column='Concepto', blank=True, null=True)  # Field name made lowercase.
    tipodocingreso = models.TextField(db_column='TipoDocIngreso', blank=True, null=True)  # Field name made lowercase.
    numidingreso = models.TextField(db_column='NumIdIngreso', blank=True, null=True)  # Field name made lowercase.
    dv = models.TextField(db_column='DV', blank=True, null=True)  # Field name made lowercase.
    primerapellidoingreso = models.TextField(db_column='PrimerApellidoIngreso', blank=True, null=True)  # Field name made lowercase.
    segundoapellidoingreso = models.TextField(db_column='SegundoApellidoIngreso', blank=True, null=True)  # Field name made lowercase.
    primernombreingreso = models.TextField(db_column='PrimerNombreIngreso', blank=True, null=True)  # Field name made lowercase.
    otrosnombresingreso = models.TextField(db_column='OtrosNombresIngreso', blank=True, null=True)  # Field name made lowercase.
    razonsocialingreso = models.TextField(db_column='RazonSocialIngreso', blank=True, null=True)  # Field name made lowercase.
    paisresidenciaingreso = models.TextField(db_column='PaisResidenciaIngreso', blank=True, null=True)  # Field name made lowercase.
    valortotaloperacion = models.TextField(db_column='ValorTotalOperacion', blank=True, null=True)  # Field name made lowercase.
    valoringresoreintegrado = models.TextField(db_column='ValorIngresoReintegrado', blank=True, null=True)  # Field name made lowercase.
    valorretencionreintegrada = models.TextField(db_column='ValorRetencionReintegrada', blank=True, null=True)  # Field name made lowercase.
    tipodoctercero = models.TextField(db_column='TipoDocTercero', blank=True, null=True)  # Field name made lowercase.
    numidtercero = models.TextField(db_column='NumIdTercero', blank=True, null=True)  # Field name made lowercase.
    primerapellidotercero = models.TextField(db_column='PrimerApellidoTercero', blank=True, null=True)  # Field name made lowercase.
    segundoapellidotercero = models.TextField(db_column='SegundoApellidoTercero', blank=True, null=True)  # Field name made lowercase.
    primernombretercero = models.TextField(db_column='PrimerNombreTercero', blank=True, null=True)  # Field name made lowercase.
    otrosnombrestercero = models.TextField(db_column='OtrosNombresTercero', blank=True, null=True)  # Field name made lowercase.
    razonsocialtercero = models.TextField(db_column='RazonSocialTercero', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    coddpto = models.TextField(db_column='CodDpto', blank=True, null=True)  # Field name made lowercase.
    codmcp = models.TextField(db_column='CodMcp', blank=True, null=True)  # Field name made lowercase.
    paisresidenciatercero = models.TextField(db_column='PaisResidenciaTercero', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_1647'


class Formato2275(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    concepto = models.TextField(db_column='Concepto', blank=True, null=True)  # Field name made lowercase.
    tipodoctercero = models.TextField(db_column='TipoDocTercero', blank=True, null=True)  # Field name made lowercase.
    numidtercero = models.TextField(db_column='NumIdTercero', blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.TextField(db_column='PrimerApellido', blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.TextField(db_column='SegundoApellido', blank=True, null=True)  # Field name made lowercase.
    primernombre = models.TextField(db_column='PrimerNombre', blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.TextField(db_column='OtrosNombres', blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.TextField(db_column='RazonSocial', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    coddpto = models.TextField(db_column='CodDpto', blank=True, null=True)  # Field name made lowercase.
    codmcp = models.TextField(db_column='CodMcp', blank=True, null=True)  # Field name made lowercase.
    codpais = models.TextField(db_column='CodPais', blank=True, null=True)  # Field name made lowercase.
    correoelectronico = models.TextField(db_column='CorreoElectronico', blank=True, null=True)  # Field name made lowercase.
    valoringresonorenta = models.TextField(db_column='ValorIngresoNoRenta', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_2275'


class Formato2276(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    entidadinformante = models.CharField(db_column='EntidadInformante', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numid = models.CharField(db_column='NumId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.CharField(db_column='OtrosNombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    coddpto = models.CharField(db_column='CodDpto', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codmcp = models.CharField(db_column='CodMcp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    paisresidencia = models.CharField(db_column='PaisResidencia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    salarios = models.BigIntegerField(db_column='Salarios', blank=True, null=True)  # Field name made lowercase.
    emolecles = models.BigIntegerField(db_column='EmolEcles', blank=True, null=True)  # Field name made lowercase.
    bonosserv = models.BigIntegerField(db_column='BonosServ', blank=True, null=True)  # Field name made lowercase.
    excesoalim = models.BigIntegerField(db_column='ExcesoAlim', blank=True, null=True)  # Field name made lowercase.
    honorarios = models.BigIntegerField(db_column='Honorarios', blank=True, null=True)  # Field name made lowercase.
    servicios = models.BigIntegerField(db_column='Servicios', blank=True, null=True)  # Field name made lowercase.
    comisiones = models.BigIntegerField(db_column='Comisiones', blank=True, null=True)  # Field name made lowercase.
    prestaciones = models.BigIntegerField(db_column='Prestaciones', blank=True, null=True)  # Field name made lowercase.
    viaticos = models.BigIntegerField(db_column='Viaticos', blank=True, null=True)  # Field name made lowercase.
    gastosrep = models.BigIntegerField(db_column='GastosRep', blank=True, null=True)  # Field name made lowercase.
    comptrabajo = models.BigIntegerField(db_column='CompTrabajo', blank=True, null=True)  # Field name made lowercase.
    apoyoecon = models.BigIntegerField(db_column='ApoyoEcon', blank=True, null=True)  # Field name made lowercase.
    otrospagos = models.BigIntegerField(db_column='OtrosPagos', blank=True, null=True)  # Field name made lowercase.
    cesintereses = models.BigIntegerField(db_column='CesIntereses', blank=True, null=True)  # Field name made lowercase.
    cesfondo = models.BigIntegerField(db_column='CesFondo', blank=True, null=True)  # Field name made lowercase.
    auxces = models.BigIntegerField(db_column='AuxCes', blank=True, null=True)  # Field name made lowercase.
    pensiones = models.BigIntegerField(db_column='Pensiones', blank=True, null=True)  # Field name made lowercase.
    ingresosbrutos = models.BigIntegerField(db_column='IngresosBrutos', blank=True, null=True)  # Field name made lowercase.
    aportesalud = models.BigIntegerField(db_column='AporteSalud', blank=True, null=True)  # Field name made lowercase.
    aportepens = models.BigIntegerField(db_column='AportePens', blank=True, null=True)  # Field name made lowercase.
    aporterais = models.BigIntegerField(db_column='AporteRAIS', blank=True, null=True)  # Field name made lowercase.
    aportepensvol = models.BigIntegerField(db_column='AportePensVol', blank=True, null=True)  # Field name made lowercase.
    aporteafc = models.BigIntegerField(db_column='AporteAFC', blank=True, null=True)  # Field name made lowercase.
    aporteavc = models.BigIntegerField(db_column='AporteAVC', blank=True, null=True)  # Field name made lowercase.
    retrentas = models.BigIntegerField(db_column='RetRentas', blank=True, null=True)  # Field name made lowercase.
    ivacosto = models.BigIntegerField(db_column='IvaCosto', blank=True, null=True)  # Field name made lowercase.
    retiva = models.BigIntegerField(db_column='RetIva', blank=True, null=True)  # Field name made lowercase.
    alim41 = models.BigIntegerField(db_column='Alim41', blank=True, null=True)  # Field name made lowercase.
    ultimos6meses = models.BigIntegerField(db_column='Ultimos6Meses', blank=True, null=True)  # Field name made lowercase.
    tipodocdependiente = models.BigIntegerField(db_column='TipoDocDependiente', blank=True, null=True)  # Field name made lowercase.
    numiddependiente = models.BigIntegerField(db_column='NumIdDependiente', blank=True, null=True)  # Field name made lowercase.
    numidfideicomiso = models.BigIntegerField(db_column='NumIdFideicomiso', blank=True, null=True)  # Field name made lowercase.
    tipodocparticipante = models.BigIntegerField(db_column='TipoDocParticipante', blank=True, null=True)  # Field name made lowercase.
    numidparticipante = models.BigIntegerField(db_column='NumIdParticipante', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formato_2276'


class Formulas(models.Model):
    idformula = models.IntegerField(db_column='IdFormula', primary_key=True)  # Field name made lowercase.
    formula = models.TextField(db_column='Formula', blank=True, null=True)  # Field name made lowercase.
    valor = models.TextField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formulas'


class InformacionTerceros(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    razonsocial = models.TextField(db_column='RazonSocial', blank=True, null=True)  # Field name made lowercase.
    headquarteraddress = models.TextField(db_column='HeadquarterAddress', blank=True, null=True)  # Field name made lowercase.
    headquartercountry = models.TextField(db_column='HeadquarterCountry', blank=True, null=True)  # Field name made lowercase.
    headquartercity = models.TextField(db_column='HeadquarterCity', blank=True, null=True)  # Field name made lowercase.
    headquarteridnumber = models.TextField(db_column='HeadquarterIdNumber', blank=True, null=True)  # Field name made lowercase.
    colombiaaddress = models.TextField(db_column='ColombiaAddress', blank=True, null=True)  # Field name made lowercase.
    colombiacity = models.TextField(db_column='ColombiaCity', blank=True, null=True)  # Field name made lowercase.
    colombianit = models.TextField(db_column='ColombiaNit', blank=True, null=True)  # Field name made lowercase.
    numid = models.TextField(db_column='NumId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'informacion_terceros'


class Municipio(models.Model):
    idmunicipio = models.IntegerField(db_column='IdMunicipio', primary_key=True)  # Field name made lowercase. The composite primary key (IdMunicipio, IdDepartamento) found, that is not supported. The first column is selected.
    nombremunicipio = models.TextField(db_column='NombreMunicipio', blank=True, null=True)  # Field name made lowercase.
    homologacion = models.TextField(db_column='Homologacion', blank=True, null=True)  # Field name made lowercase.
    iddepartamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='IdDepartamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'municipio'
        unique_together = (('idmunicipio', 'iddepartamento'),)


class Pais(models.Model):
    idpais = models.IntegerField(db_column='IdPais', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    homologacion = models.TextField(db_column='Homologacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pais'


class PersonaNatural(models.Model):
    numid = models.CharField(db_column='NumId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=3, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.TextField(db_column='PrimerApellido', blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.TextField(db_column='SegundoApellido', blank=True, null=True)  # Field name made lowercase.
    primernombre = models.TextField(db_column='PrimerNombre', blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.TextField(db_column='OtrosNombres', blank=True, null=True)  # Field name made lowercase.
    encontradodian = models.CharField(db_column='EncontradoDian', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona_natural'


class Planillas(models.Model):
    idplanillas = models.AutoField(db_column='idPlanillas', primary_key=True)  # Field name made lowercase.
    a = models.TextField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    riesgo = models.TextField(db_column='Riesgo', blank=True, null=True)  # Field name made lowercase.
    c = models.TextField(db_column='C', blank=True, null=True)  # Field name made lowercase.
    d = models.TextField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    e = models.TextField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    f = models.TextField(db_column='F', blank=True, null=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    h = models.TextField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    i = models.TextField(db_column='I', blank=True, null=True)  # Field name made lowercase.
    j = models.TextField(db_column='J', blank=True, null=True)  # Field name made lowercase.
    k = models.TextField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    m = models.TextField(db_column='M', blank=True, null=True)  # Field name made lowercase.
    n = models.TextField(db_column='N', blank=True, null=True)  # Field name made lowercase.
    o = models.TextField(db_column='O', blank=True, null=True)  # Field name made lowercase.
    p = models.TextField(db_column='P', blank=True, null=True)  # Field name made lowercase.
    q = models.TextField(db_column='Q', blank=True, null=True)  # Field name made lowercase.
    r = models.TextField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    s = models.TextField(db_column='S', blank=True, null=True)  # Field name made lowercase.
    t = models.TextField(db_column='T', blank=True, null=True)  # Field name made lowercase.
    u = models.TextField(db_column='U', blank=True, null=True)  # Field name made lowercase.
    v = models.TextField(db_column='V', blank=True, null=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    x = models.TextField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.TextField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    z = models.TextField(db_column='Z', blank=True, null=True)  # Field name made lowercase.
    aa = models.TextField(db_column='AA', blank=True, null=True)  # Field name made lowercase.
    ab = models.TextField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    valorapagar = models.TextField(db_column='ValorAPagar', blank=True, null=True)  # Field name made lowercase.
    ad = models.TextField(db_column='AD', blank=True, null=True)  # Field name made lowercase.
    ae = models.TextField(db_column='AE', blank=True, null=True)  # Field name made lowercase.
    af = models.TextField(db_column='AF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planillas'


class Planillas1011(models.Model):
    idplanilla = models.AutoField(db_column='idPlanilla', primary_key=True)  # Field name made lowercase.
    a = models.TextField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    b = models.TextField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    c = models.TextField(db_column='C', blank=True, null=True)  # Field name made lowercase.
    d = models.TextField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    e = models.TextField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    f = models.TextField(db_column='F', blank=True, null=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    h = models.TextField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    i = models.TextField(db_column='I', blank=True, null=True)  # Field name made lowercase.
    j = models.TextField(db_column='J', blank=True, null=True)  # Field name made lowercase.
    k = models.TextField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    m = models.TextField(db_column='M', blank=True, null=True)  # Field name made lowercase.
    n = models.TextField(db_column='N', blank=True, null=True)  # Field name made lowercase.
    o = models.TextField(db_column='O', blank=True, null=True)  # Field name made lowercase.
    p = models.TextField(db_column='P', blank=True, null=True)  # Field name made lowercase.
    q = models.TextField(db_column='Q', blank=True, null=True)  # Field name made lowercase.
    r = models.TextField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    s = models.TextField(db_column='S', blank=True, null=True)  # Field name made lowercase.
    t = models.TextField(db_column='T', blank=True, null=True)  # Field name made lowercase.
    u = models.TextField(db_column='U', blank=True, null=True)  # Field name made lowercase.
    v = models.TextField(db_column='V', blank=True, null=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    x = models.TextField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.TextField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    z = models.TextField(db_column='Z', blank=True, null=True)  # Field name made lowercase.
    aa = models.TextField(db_column='AA', blank=True, null=True)  # Field name made lowercase.
    ab = models.TextField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    ac = models.TextField(db_column='AC', blank=True, null=True)  # Field name made lowercase.
    ad = models.TextField(db_column='AD', blank=True, null=True)  # Field name made lowercase.
    ae = models.TextField(db_column='AE', blank=True, null=True)  # Field name made lowercase.
    af = models.TextField(db_column='AF', blank=True, null=True)  # Field name made lowercase.
    ag = models.TextField(db_column='AG', blank=True, null=True)  # Field name made lowercase.
    ah = models.TextField(db_column='AH', blank=True, null=True)  # Field name made lowercase.
    ai = models.TextField(db_column='AI', blank=True, null=True)  # Field name made lowercase.
    aj = models.TextField(db_column='AJ', blank=True, null=True)  # Field name made lowercase.
    ak = models.TextField(db_column='AK', blank=True, null=True)  # Field name made lowercase.
    al = models.TextField(db_column='AL', blank=True, null=True)  # Field name made lowercase.
    am = models.TextField(db_column='AM', blank=True, null=True)  # Field name made lowercase.
    an = models.TextField(db_column='AN', blank=True, null=True)  # Field name made lowercase.
    ao = models.TextField(db_column='AO', blank=True, null=True)  # Field name made lowercase.
    ap = models.TextField(db_column='AP', blank=True, null=True)  # Field name made lowercase.
    aq = models.TextField(db_column='AQ', blank=True, null=True)  # Field name made lowercase.
    ar = models.TextField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    as_field = models.TextField(db_column='AS', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    at = models.TextField(db_column='AT', blank=True, null=True)  # Field name made lowercase.
    au = models.TextField(db_column='AU', blank=True, null=True)  # Field name made lowercase.
    av = models.TextField(db_column='AV', blank=True, null=True)  # Field name made lowercase.
    aw = models.TextField(db_column='AW', blank=True, null=True)  # Field name made lowercase.
    ax = models.TextField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    ay = models.TextField(db_column='AY', blank=True, null=True)  # Field name made lowercase.
    az = models.TextField(db_column='AZ', blank=True, null=True)  # Field name made lowercase.
    ba = models.TextField(db_column='BA', blank=True, null=True)  # Field name made lowercase.
    bb = models.TextField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    bc = models.TextField(db_column='BC', blank=True, null=True)  # Field name made lowercase.
    bd = models.TextField(db_column='BD', blank=True, null=True)  # Field name made lowercase.
    be = models.TextField(db_column='BE', blank=True, null=True)  # Field name made lowercase.
    bf = models.TextField(db_column='BF', blank=True, null=True)  # Field name made lowercase.
    bg = models.TextField(db_column='BG', blank=True, null=True)  # Field name made lowercase.
    bh = models.TextField(db_column='BH', blank=True, null=True)  # Field name made lowercase.
    bi = models.TextField(db_column='BI', blank=True, null=True)  # Field name made lowercase.
    bj = models.TextField(db_column='BJ', blank=True, null=True)  # Field name made lowercase.
    bk = models.TextField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    bl = models.TextField(db_column='BL', blank=True, null=True)  # Field name made lowercase.
    bm = models.TextField(db_column='BM', blank=True, null=True)  # Field name made lowercase.
    bn = models.TextField(db_column='BN', blank=True, null=True)  # Field name made lowercase.
    bo = models.TextField(db_column='BO', blank=True, null=True)  # Field name made lowercase.
    bp = models.TextField(db_column='BP', blank=True, null=True)  # Field name made lowercase.
    bq = models.TextField(db_column='BQ', blank=True, null=True)  # Field name made lowercase.
    br = models.TextField(db_column='BR', blank=True, null=True)  # Field name made lowercase.
    bs = models.TextField(db_column='BS', blank=True, null=True)  # Field name made lowercase.
    bt = models.TextField(db_column='BT', blank=True, null=True)  # Field name made lowercase.
    bu = models.TextField(db_column='BU', blank=True, null=True)  # Field name made lowercase.
    bv = models.TextField(db_column='BV', blank=True, null=True)  # Field name made lowercase.
    bw = models.TextField(db_column='BW', blank=True, null=True)  # Field name made lowercase.
    bx = models.TextField(db_column='BX', blank=True, null=True)  # Field name made lowercase.
    by = models.TextField(db_column='BY', blank=True, null=True)  # Field name made lowercase.
    bz = models.TextField(db_column='BZ', blank=True, null=True)  # Field name made lowercase.
    ca = models.TextField(db_column='CA', blank=True, null=True)  # Field name made lowercase.
    cb = models.TextField(db_column='CB', blank=True, null=True)  # Field name made lowercase.
    cc = models.TextField(db_column='CC', blank=True, null=True)  # Field name made lowercase.
    cd = models.TextField(db_column='CD', blank=True, null=True)  # Field name made lowercase.
    ce = models.TextField(db_column='CE', blank=True, null=True)  # Field name made lowercase.
    cf = models.TextField(db_column='CF', blank=True, null=True)  # Field name made lowercase.
    cg = models.TextField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    ch = models.TextField(db_column='CH', blank=True, null=True)  # Field name made lowercase.
    ci = models.TextField(db_column='CI', blank=True, null=True)  # Field name made lowercase.
    cj = models.TextField(db_column='CJ', blank=True, null=True)  # Field name made lowercase.
    ck = models.TextField(db_column='CK', blank=True, null=True)  # Field name made lowercase.
    cl = models.TextField(db_column='CL', blank=True, null=True)  # Field name made lowercase.
    cm = models.TextField(db_column='CM', blank=True, null=True)  # Field name made lowercase.
    cn = models.TextField(db_column='CN', blank=True, null=True)  # Field name made lowercase.
    co = models.TextField(db_column='CO', blank=True, null=True)  # Field name made lowercase.
    cp = models.TextField(db_column='CP', blank=True, null=True)  # Field name made lowercase.
    cq = models.TextField(db_column='CQ', blank=True, null=True)  # Field name made lowercase.
    cr = models.TextField(db_column='CR', blank=True, null=True)  # Field name made lowercase.
    cs = models.TextField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    ct = models.TextField(db_column='CT', blank=True, null=True)  # Field name made lowercase.
    cu = models.TextField(db_column='CU', blank=True, null=True)  # Field name made lowercase.
    cv = models.TextField(db_column='CV', blank=True, null=True)  # Field name made lowercase.
    cw = models.TextField(db_column='CW', blank=True, null=True)  # Field name made lowercase.
    cx = models.TextField(db_column='CX', blank=True, null=True)  # Field name made lowercase.
    cy = models.TextField(db_column='CY', blank=True, null=True)  # Field name made lowercase.
    cz = models.TextField(db_column='CZ', blank=True, null=True)  # Field name made lowercase.
    da = models.TextField(db_column='DA', blank=True, null=True)  # Field name made lowercase.
    db = models.TextField(db_column='DB', blank=True, null=True)  # Field name made lowercase.
    dc = models.TextField(db_column='DC', blank=True, null=True)  # Field name made lowercase.
    dd = models.TextField(db_column='DD', blank=True, null=True)  # Field name made lowercase.
    de = models.TextField(db_column='DE', blank=True, null=True)  # Field name made lowercase.
    df = models.TextField(db_column='DF', blank=True, null=True)  # Field name made lowercase.
    dg = models.TextField(db_column='DG', blank=True, null=True)  # Field name made lowercase.
    dh = models.TextField(db_column='DH', blank=True, null=True)  # Field name made lowercase.
    di = models.TextField(db_column='DI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planillas_1011'


class PlanillasResumen(models.Model):
    idplanillas_empleado = models.AutoField(primary_key=True)
    razonsocial = models.BigIntegerField(db_column='RazonSocial', blank=True, null=True)  # Field name made lowercase.
    enero = models.BigIntegerField(db_column='Enero', blank=True, null=True)  # Field name made lowercase.
    febrero = models.BigIntegerField(db_column='Febrero', blank=True, null=True)  # Field name made lowercase.
    marzo = models.BigIntegerField(db_column='Marzo', blank=True, null=True)  # Field name made lowercase.
    abril = models.BigIntegerField(db_column='Abril', blank=True, null=True)  # Field name made lowercase.
    mayo = models.BigIntegerField(db_column='Mayo', blank=True, null=True)  # Field name made lowercase.
    junio = models.BigIntegerField(db_column='Junio', blank=True, null=True)  # Field name made lowercase.
    julio = models.BigIntegerField(db_column='Julio', blank=True, null=True)  # Field name made lowercase.
    agosto = models.BigIntegerField(db_column='Agosto', blank=True, null=True)  # Field name made lowercase.
    septiembre = models.BigIntegerField(db_column='Septiembre', blank=True, null=True)  # Field name made lowercase.
    octubre = models.BigIntegerField(db_column='Octubre', blank=True, null=True)  # Field name made lowercase.
    noviembre = models.BigIntegerField(db_column='Noviembre', blank=True, null=True)  # Field name made lowercase.
    diciembre = models.BigIntegerField(db_column='Diciembre', blank=True, null=True)  # Field name made lowercase.
    totales = models.CharField(db_column='Totales', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planillas_resumen'


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


class RetencionesAsumidas(models.Model):
    idretenciones = models.IntegerField(db_column='IdRetenciones', primary_key=True)  # Field name made lowercase.
    cuentaprincipial = models.CharField(db_column='CuentaPrincipial', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cuentasecundaria = models.CharField(db_column='CuentaSecundaria', max_length=45, blank=True, null=True)  # Field name made lowercase.
    columna = models.CharField(db_column='Columna', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='IdCliente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'retenciones_asumidas'


class Rues(models.Model):
    idrues = models.AutoField(db_column='IdRues', primary_key=True)  # Field name made lowercase.
    orgjuridica = models.TextField(db_column='OrgJuridica', blank=True, null=True)  # Field name made lowercase.
    categoria = models.TextField(db_column='Categoria', blank=True, null=True)  # Field name made lowercase.
    fechamatricula = models.TextField(db_column='FechaMatricula', blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.TextField(db_column='RazonSocial', blank=True, null=True)  # Field name made lowercase.
    tipoidentificacion = models.TextField(db_column='TipoIdentificacion', blank=True, null=True)  # Field name made lowercase.
    numeroidentificacion = models.TextField(db_column='NumeroIdentificacion', blank=True, null=True)  # Field name made lowercase.
    actividadeconomica = models.TextField(db_column='ActividadEconomica', blank=True, null=True)  # Field name made lowercase.
    actividadeconomica2 = models.TextField(db_column='ActividadEconomica2', blank=True, null=True)  # Field name made lowercase.
    actividadeconomica3 = models.TextField(db_column='ActividadEconomica3', blank=True, null=True)  # Field name made lowercase.
    actividadeconomica4 = models.TextField(db_column='ActividadEconomica4', blank=True, null=True)  # Field name made lowercase.
    desctamanoempresa = models.TextField(db_column='DescTamanoEmpresa', blank=True, null=True)  # Field name made lowercase.
    departamento = models.TextField(db_column='Departamento', blank=True, null=True)  # Field name made lowercase.
    municipio = models.TextField(db_column='Municipio', blank=True, null=True)  # Field name made lowercase.
    direccioncomercial = models.TextField(db_column='DireccionComercial', blank=True, null=True)  # Field name made lowercase.
    correocomercial = models.TextField(db_column='CorreoComercial', blank=True, null=True)  # Field name made lowercase.
    replegal = models.TextField(db_column='RepLegal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rues'


class SeguridadSocial(models.Model):
    idseguridadsocial = models.AutoField(db_column='IdSeguridadSocial', primary_key=True)  # Field name made lowercase.
    seguridadsocial = models.CharField(db_column='SeguridadSocial', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seguridad_social'


class Sistema(models.Model):
    idsistema = models.IntegerField(db_column='idSistema', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sistema'


class TercerosAliaddo(models.Model):
    razonsocial = models.TextField(db_column='RazonSocial', blank=True, null=True)  # Field name made lowercase.
    tipoid = models.TextField(db_column='TipoId', blank=True, null=True)  # Field name made lowercase.
    identificacion = models.TextField(db_column='Identificacion', blank=True, null=True)  # Field name made lowercase.
    dv = models.TextField(db_column='DV', blank=True, null=True)  # Field name made lowercase.
    tipo = models.TextField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    codigodelaresponsabilidadfiscal = models.TextField(db_column='CodigoDeLaResponsabilidadFiscal', blank=True, null=True)  # Field name made lowercase.
    codigoderesponsablede = models.TextField(db_column='CodigoDeResponsableDe', blank=True, null=True)  # Field name made lowercase.
    lehacesretencionenlafuente = models.TextField(db_column='LeHacesRetencionEnLaFuente', blank=True, null=True)  # Field name made lowercase.
    tehacenretencionenlafuente = models.TextField(db_column='TeHacenRetencionEnLaFuente', blank=True, null=True)  # Field name made lowercase.
    primernombre = models.TextField(db_column='PrimerNombre', blank=True, null=True)  # Field name made lowercase.
    segundonombre = models.TextField(db_column='SegundoNombre', blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.TextField(db_column='PrimerApellido', blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.TextField(db_column='SegundoApellido', blank=True, null=True)  # Field name made lowercase.
    codigodelaactividadeconomica = models.TextField(db_column='CodigoDeLaActividadEconomica', blank=True, null=True)  # Field name made lowercase.
    telefonoprincipal = models.TextField(db_column='TelefonoPrincipal', blank=True, null=True)  # Field name made lowercase.
    otrotelefono1 = models.TextField(db_column='OtroTelefono1', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    esdelexterior = models.TextField(db_column='EsDelExterior', blank=True, null=True)  # Field name made lowercase.
    cliente = models.TextField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    proveedor = models.TextField(db_column='Proveedor', blank=True, null=True)  # Field name made lowercase.
    propietario = models.TextField(db_column='Propietario', blank=True, null=True)  # Field name made lowercase.
    cuentaparacausarlasventas = models.TextField(db_column='CuentaParaCausarLasVentas', blank=True, null=True)  # Field name made lowercase.
    cuentaparacausarlascompras = models.TextField(db_column='CuentaParaCausarLasCompras', blank=True, null=True)  # Field name made lowercase.
    cuentaparacausarlosgastos = models.TextField(db_column='CuentaParaCausarLosGastos', blank=True, null=True)  # Field name made lowercase.
    etiqueta = models.TextField(db_column='Etiqueta', blank=True, null=True)  # Field name made lowercase.
    vendedorasignado = models.TextField(db_column='VendedorAsignado', blank=True, null=True)  # Field name made lowercase.
    aplicaretencionica = models.TextField(db_column='AplicaRetencionIca', blank=True, null=True)  # Field name made lowercase.
    tarifaicacompra = models.TextField(db_column='TarifaIcaCompra', blank=True, null=True)  # Field name made lowercase.
    cuentaicacompra = models.TextField(db_column='CuentaIcaCompra', blank=True, null=True)  # Field name made lowercase.
    tarifaretencionivaventa = models.TextField(db_column='TarifaRetencionIvaVenta', blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.TextField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    ingresosanuales = models.TextField(db_column='IngresosAnuales', blank=True, null=True)  # Field name made lowercase.
    numeroempleados = models.TextField(db_column='NumeroEmpleados', blank=True, null=True)  # Field name made lowercase.
    moneda = models.TextField(db_column='Moneda', blank=True, null=True)  # Field name made lowercase.
    cupodecredito = models.TextField(db_column='CupoDeCredito', blank=True, null=True)  # Field name made lowercase.
    diascredito = models.TextField(db_column='DiasCredito', blank=True, null=True)  # Field name made lowercase.
    banco = models.TextField(db_column='Banco', blank=True, null=True)  # Field name made lowercase.
    tipodecuenta = models.TextField(db_column='TipoDeCuenta', blank=True, null=True)  # Field name made lowercase.
    numerodecuenta = models.TextField(db_column='NumeroDeCuenta', blank=True, null=True)  # Field name made lowercase.
    nombredireccion = models.TextField(db_column='NombreDireccion', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    pais = models.TextField(db_column='Pais', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    ciudad = models.TextField(db_column='Ciudad', blank=True, null=True)  # Field name made lowercase.
    barrio = models.TextField(db_column='Barrio', blank=True, null=True)  # Field name made lowercase.
    otrotelefono = models.TextField(db_column='otroTelefono', blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.TextField(db_column='CodigoPostal', blank=True, null=True)  # Field name made lowercase.
    fechadecreacion = models.TextField(db_column='FechaDeCreacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'terceros_aliaddo'


class TercerosAllegra(models.Model):
    tipodecontacto = models.TextField(db_column='TipoDeContacto', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    segundonombre = models.TextField(db_column='SegundoNombre', blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.TextField(db_column='PrimerApellido', blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.TextField(db_column='SegundoApellido', blank=True, null=True)  # Field name made lowercase.
    tipodeidentificacion = models.TextField(db_column='TipoDeIdentificacion', blank=True, null=True)  # Field name made lowercase.
    identificacion = models.TextField(db_column='Identificacion', blank=True, null=True)  # Field name made lowercase.
    digitodeverificacion = models.TextField(db_column='DigitoDeVerificacion', blank=True, null=True)  # Field name made lowercase.
    tipodepersona = models.TextField(db_column='TipoDePersona', blank=True, null=True)  # Field name made lowercase.
    responsabilidadtributaria = models.TextField(db_column='ResponsabilidadTributaria', blank=True, null=True)  # Field name made lowercase.
    telefono1 = models.TextField(db_column='Telefono1', blank=True, null=True)  # Field name made lowercase.
    telefono2 = models.TextField(db_column='Telefono2', blank=True, null=True)  # Field name made lowercase.
    celular = models.TextField(db_column='Celular', blank=True, null=True)  # Field name made lowercase.
    pais = models.TextField(db_column='Pais', blank=True, null=True)  # Field name made lowercase.
    departamento = models.TextField(db_column='Departamento', blank=True, null=True)  # Field name made lowercase.
    municipio = models.TextField(db_column='Municipio', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.TextField(db_column='CodigoPostal', blank=True, null=True)  # Field name made lowercase.
    correosecundario = models.TextField(db_column='CorreoSecundario', blank=True, null=True)  # Field name made lowercase.
    correo = models.TextField(db_column='Correo', blank=True, null=True)  # Field name made lowercase.
    listadeprecios = models.TextField(db_column='ListaDePrecios', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.TextField(db_column='Vendedor', blank=True, null=True)  # Field name made lowercase.
    plazodepago = models.TextField(db_column='PlazoDePago', blank=True, null=True)  # Field name made lowercase.
    cuentasporcobrar = models.TextField(db_column='CuentasPorCobrar', blank=True, null=True)  # Field name made lowercase.
    cuentasporpagar = models.TextField(db_column='CuentasPorPagar', blank=True, null=True)  # Field name made lowercase.
    limitedecredito = models.TextField(db_column='LimiteDeCredito', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'terceros_allegra'


class TercerosAvansys(models.Model):
    id_1 = models.TextField(db_column='Id_1', blank=True, null=True)  # Field name made lowercase.
    identificationdocument = models.TextField(db_column='IdentificationDocument', blank=True, null=True)  # Field name made lowercase.
    idnumbers = models.TextField(db_column='IdNumbers', blank=True, null=True)  # Field name made lowercase.
    checkdigit = models.TextField(db_column='CheckDigit', blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.TextField(db_column='PrimerApellido', blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.TextField(db_column='SegundoApellido', blank=True, null=True)  # Field name made lowercase.
    primernombre = models.TextField(db_column='PrimerNombre', blank=True, null=True)  # Field name made lowercase.
    otrosnombres = models.TextField(db_column='OtrosNombres', blank=True, null=True)  # Field name made lowercase.
    commercialname = models.TextField(db_column='CommercialName', blank=True, null=True)  # Field name made lowercase.
    emailbounced = models.TextField(db_column='EmailBounced', blank=True, null=True)  # Field name made lowercase.
    contactaddress = models.TextField(db_column='ContactAddress', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    countryid = models.TextField(db_column='CountryId', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    reftypeid = models.TextField(db_column='RefTypeId', blank=True, null=True)  # Field name made lowercase.
    documenttypeid = models.TextField(db_column='DocumentTypeId', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    cityid = models.TextField(db_column='CityId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'terceros_avansys'


class TercerosSiigoNube(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombretercero = models.TextField(db_column='NombreTercero', blank=True, null=True)  # Field name made lowercase.
    tipodeidentificacion = models.TextField(db_column='TipoDeIdentificacion', blank=True, null=True)  # Field name made lowercase.
    identificacion = models.CharField(db_column='Identificacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    digitoverificacion = models.TextField(db_column='DigitoVerificacion', blank=True, null=True)  # Field name made lowercase.
    sucursal = models.TextField(db_column='Sucursal', blank=True, null=True)  # Field name made lowercase.
    tipoderegimeniva = models.TextField(db_column='TipoDeRegimenIVA', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    ciudad = models.TextField(db_column='Ciudad', blank=True, null=True)  # Field name made lowercase.
    telefono = models.TextField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    nombrescontacto = models.TextField(db_column='NombresContacto', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    codpais = models.CharField(db_column='CodPais', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'terceros_siigo_nube'


class TercerosSiigoPyme(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nit = models.TextField(db_column='Nit', blank=True, null=True)  # Field name made lowercase.
    sucursal = models.TextField(db_column='Sucursal', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    contacto = models.TextField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    pais = models.TextField(db_column='Pais', blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono1 = models.TextField(db_column='Telefono1', blank=True, null=True)  # Field name made lowercase.
    telefono2 = models.TextField(db_column='Telefono2', blank=True, null=True)  # Field name made lowercase.
    telefono3 = models.TextField(db_column='Telefono3', blank=True, null=True)  # Field name made lowercase.
    telefono4 = models.TextField(db_column='Telefono4', blank=True, null=True)  # Field name made lowercase.
    celular = models.TextField(db_column='Celular', blank=True, null=True)  # Field name made lowercase.
    fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    apartado = models.TextField(db_column='Apartado', blank=True, null=True)  # Field name made lowercase.
    cupo = models.TextField(db_column='Cupo', blank=True, null=True)  # Field name made lowercase.
    precio = models.TextField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.
    califica = models.TextField(db_column='Califica', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    cumple = models.TextField(db_column='Cumple', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.TextField(db_column='Vendedor', blank=True, null=True)  # Field name made lowercase.
    tipo = models.TextField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    digito = models.TextField(db_column='Digito', blank=True, null=True)  # Field name made lowercase.
    clasific = models.TextField(db_column='Clasific', blank=True, null=True)  # Field name made lowercase.
    fpago = models.TextField(db_column='FPago', blank=True, null=True)  # Field name made lowercase.
    perpago = models.TextField(db_column='PerPago', blank=True, null=True)  # Field name made lowercase.
    activida = models.TextField(db_column='Activida', blank=True, null=True)  # Field name made lowercase.
    descuento = models.TextField(db_column='Descuento', blank=True, null=True)  # Field name made lowercase.
    tipopersona = models.CharField(db_column='TipoPersona', max_length=100, blank=True, null=True)  # Field name made lowercase.
    declarante = models.TextField(db_column='Declarante', blank=True, null=True)  # Field name made lowercase.
    agenteretenedor = models.TextField(db_column='AgenteRetenedor', blank=True, null=True)  # Field name made lowercase.
    autorretenedor = models.TextField(db_column='Autorretenedor', blank=True, null=True)  # Field name made lowercase.
    benrte = models.TextField(db_column='BenRte', blank=True, null=True)  # Field name made lowercase.
    agerte = models.TextField(db_column='AgeRte', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    tipsoc = models.TextField(db_column='TipSoc', blank=True, null=True)  # Field name made lowercase.
    contactofacturacion = models.TextField(db_column='ContactoFacturacion', blank=True, null=True)  # Field name made lowercase.
    mailcontactofacturacion = models.TextField(db_column='MailContactoFacturacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'terceros_siigo_pyme'


class TipoDoc(models.Model):
    idtipodoc = models.IntegerField(db_column='IdTipoDoc', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    homologacion = models.TextField(db_column='Homologacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_doc'


class TipoInformante(models.Model):
    idtipoinformate = models.IntegerField(db_column='IdTipoInformate', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_informante'
