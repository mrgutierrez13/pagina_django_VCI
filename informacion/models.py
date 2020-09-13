from django.db import models

# Create your models here.
# CONSEJO: Sacar las fecha como nombre:
# https://stackoverflow.com/questions/9621388/django-how-to-get-month-name
# CONSEJO: Manejar Fechas
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-date-based/#montharchiveview
# CONSEJO: Utilizar REGEX y remover lineas contienen Ej. contenido  ===>  ^.*contenido.*$\n


class Boletin(models.Model):
    """Modelo representando un boletin a subir a la pagina"""
    titulo = models.CharField(max_length=200)
    portada = models.ImageField(upload_to='images/', verbose_name="Portada del Boletin",
                                help_text='Ingresa la imagen que representara el boletin')
    archivo = models.FileField(
        upload_to='pdf/', verbose_name="Documento PDF", help_text='Ingresa un archivo PDF.')

    class Meta:
        verbose_name = 'Boletin'
        verbose_name_plural = 'Boletines'

    def __str__(self):
        """String que representa el boletin"""
        return self.titulo


class TipoNorma(models.Model):
    """Modelo representando una nueva seccion para las normas"""
    nombre_seccion = models.CharField(max_length=200,
                                      help_text="Ingresa el nombre para una nueva seccion de NORMAS.")

    class Meta:
        verbose_name = 'Tipo de Norma'
        verbose_name_plural = 'Tipos de normas'

    def __str__(self):
        """String que representa la seccion de normas"""
        return self.nombre_seccion


class Norma(models.Model):
    """Modelo representando una norma a mostrar en la seccion Normativa"""
    numero = models.CharField(max_length=20)
    fecha = models.DateField(
        verbose_name="", help_text="Ingresa la fecha en formato AÑO-MES-DIA")
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)
    seccion_de_norma = models.ForeignKey(
        'TipoNorma', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='pdf/', null=True, blank=True, verbose_name="Archivo PDF de la norma",
                               help_text='Ingresa un archivo PDF.')

    def __str__(self):
        """String que representa la norma"""
        return self.titulo


class Fideicomiso(models.Model):
    """Modelo representando un fideicomiso"""
    nombre = models.CharField(max_length=200)
    decreto = models.CharField(
        max_length=200, help_text="Ingresa el numero del decreto")
    decreto_descripcion = models.TextField(
        max_length=1000, help_text="Describe el decreto")
    finalidad = models.TextField(
        max_length=1000, help_text="Escribe la finalidad del decreto")
    beneficiario = models.TextField(
        max_length=1000, help_text="Describe los beneficiarios del fideicomiso")
    vigencia = models.DateField(
        help_text="Ingresa la fecha de vigencia del fideicomiso")

    def __str__(self):
        """String que representa el boletin"""
        return self.nombre


class Evento(models.Model):
    """Modelo representando un evento"""
    nombre = models.CharField(max_length=200)
    enlace = models.CharField(max_length=200)
    fecha = models.DateField(help_text="ingresar la fecha del evento")
    organizador = models.CharField(max_length=100)
    enlace_organizador = models.CharField(
        max_length=200, null=True, blank=True)
    tipo = models.CharField(
        max_length=200, help_text="Ingresa el tipo el feria, Ej: Multisectorial")
    descripcion = models.TextField(
        max_length=1000, help_text="Da una explicacion de la feria")
    departamento = models.CharField(
        max_length=200, help_text="Ingresa el/los departamento/s en que la feria se llevara a cabo")
    direccion = models.CharField(
        max_length=500, help_text="Ingresa la direccion del evento")
    enlace_google_maps = models.CharField(
        max_length=500, help_text="Ingresa el enlace de google maps", null=True, blank=True)

    def __str__(self):
        """String que representa el boletin"""
        return self.nombre

###########################################
#   MODELOS PARA DIRECTORIO DE PROVEEDORES
###########################################


class Departamento(models.Model):
    """Modelo de los departamentos de Bolivia"""
    nombre = models.CharField(max_length=10)


class Municipio(models.Model):
    """Modelo para el municipio en que esta una empresa"""
    nombre = models.CharField(max_length=30)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)


class Proveedor(models.Model):
    """Modelo representando un proveedor"""
    nit_ci = models.CharField(max_length=11, primary_key=True)
    razon_social = models.CharField(max_length=150)

    TIPO_DE_EMPRESA = (
        ('U', "EMPRESA UNIPERSONAL"),
        ('J', "EMPRESA JURIDICA"),
        ('P', "ENTIDAD PUBLICA"),
        ('R', "REGIMEN AGROPECUARIO UNIFICADO (RAU)"),
    )

    tipo_empresa = models.CharField(
        max_length=1,
        choices=TIPO_DE_EMPRESA,
        default='P',
        help_text='Selecciona el tipo de empresa',
    )

    TIPO_DE_SOCIETARIO = (
        ('UN', "UNIPERSONAL"),
        ('SA', "SOCIEDAD ANÓNIMA"),
        ('SR', "SOCIEDAD DE RESPONSABILIDAD LIMITADA"),
        ('UP', "UNIVERSIDAD PÚBLICA"),
        ('OT', "OTRA DIFERENTE A LAS ANTERIORES"),
        ('AR', "ASOCIACIÓN /RELIGIOSA/CULTURAL/ SOCIAL"),
        ('MI', "MINISTERIO"),
        ('FU', "FUNDACIÓN /ASOCIACIÓN SIN FINES DE LUCRO"),
        ('GO', "GOBERNACIÓN"),
        ('SU', "SUCURSAL O AGENCIA PERMANENTE DE EMPRESA CONSTITUIDA EN EL EXTERIOR"),
        ('ON', "ORGANISMO NO GUBERNAMENTAL"),
        ('SC', "SOCIEDAD CIVIL"),
        ('AM', "ALCALDIA O MUNICIPIO"),
        ('EP', "EMPRESA PÚBLICA"),
        ('CM', "COOPERATIVA - MUTUAL"),
        ('CO', "CONTRATO DE OPERACIONES"),
        ('BP', "BLOQUE PETROLERO"),
        ('OP', "ORGANIZACIONES DE PEQUEÑOS PRODUCTORES"),
        ('SM', "SOCIEDAD MIXTA"),
        ('PN', "PERSONA NATURAL"),
        ('AT', "ASOCIACIÓN DE TRANSPORTE O SINDICATO - ACCIDENTAL"),
        ('SX', "SOCIEDAD ACCIDENTAL"),
        ('SO', "SOCIEDAD COLECTIVA"),
    )

    tipo_societario = models.CharField(
        max_length=2,
        choices=TIPO_DE_SOCIETARIO,
        default='SA',
        help_text='Selecciona el tipo de societario',
    )

    nombre_contacto = models.CharField(max_length=80)
    celular = models.CharField(max_length=8, null=True, blank=True)
    email_contacto = models.CharField(max_length=50, null=True, blank=True)
    fax = models.CharField(max_length=13, null=True, blank=True)
    telefono = models.CharField(max_length=7, null=True, blank=True)
    municipio = models.ForeignKey('Municipio', on_delete=models.CASCADE)
    zona = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class PaisDestino(models.Model):
    """El pais destino de una actividad economica"""
    nombre = models.CharField(max_length=60)


class RutaProveedor(models.Model):
    """El departamento de su sucursal y el pais de la exportacion"""
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    pais = models.ForeignKey('PaisDestino', on_delete=models.CASCADE)


class ProveedorActivo(models.Model):
    """Representa una empresa con actividad economica registrada"""
    nit_ci = models.CharField(max_length=11, unique=True)
    razon_social = models.CharField(max_length=150)


class Nandina10(models.Model):
    """Los datos de nandina con 10 digitos"""
    nandina = models.CharField(max_length=10, unique=True)
    descripcion = models.CharField(max_length=600)


class Cuode3(models.Model):
    """Los datos de cuode con 3 digitos"""
    cuode = models.CharField(max_length=10, unique=True)
    descripcion = models.CharField(max_length=100)


class ActividadEconomica(models.Model):
    """Muestra la actividad economica de las empresas con registro en la DB"""
    nit_ci = models.ForeignKey('ProveedorActivo', on_delete=models.CASCADE)
    nandina = models.ForeignKey('Nandina10', on_delete=models.CASCADE)
    cuode = models.ForeignKey('Cuode3', on_delete=models.CASCADE)
    ruta = models.ForeignKey('RutaProveedor', on_delete=models.CASCADE)
    gestion = models.PositiveSmallIntegerField()
    kg_bruto = models.FloatField()
    kg_neto = models.FloatField()
    cif = models.FloatField()
