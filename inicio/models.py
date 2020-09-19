from django.db import models
from django.utils.html import mark_safe
from django.conf import settings
from colorfield.fields import ColorField


# Modelos

# TODO: VALIDACION SVG
# https://stackoverflow.com/questions/38006200/allow-svg-files-to-be-uploaded-to-imagefield-via-django-admin
# CONSEJO: PARA CREAR TABLAS EN LA BASE DE DATOS:  python manage.py migrate --run-syncdb
# CONSEJO: PARA AGREGAR COLOR-PICKER A LA BANDEJA ADMIN:  django-colorfield
# CONSEJO: Para borrar fotos/media inutilizadas en el proyecto: pip install django-cleanup
# https://stackoverflow.com/questions/21941503/django-delete-unused-media-files


class Servicio(models.Model):
    """Modelo representando la informacion de un servicio a ser mostrado en la pagina de inicio"""
    posicion = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=50)
    enlace = models.CharField(max_length=200, null=True, blank=True)
    color = ColorField(default='#F2D00D')
    descripcion = models.TextField(max_length=200,
                                   help_text='Escribe la descripcion del servicio que se vera en la pagina de inicio...')
    icono = models.FileField(upload_to='images/', verbose_name="ICONO DEL SERVICIO",
                             help_text='Ingresa una imagen formato SVG')

    def icono_tag(self):
        """Para mostrar imagenes en el panel de administracion"""
        return mark_safe('<img src="%s" width="150" height="150" />' % (settings.MEDIA_URL + self.icono.name))

    def __str__(self):
        """String que representa el servicio"""
        return self.nombre


class Libro(models.Model):
    """Modelo de un libro importante para mostrar en la pagina de inicio"""
    posicion = models.PositiveSmallIntegerField()
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')
    descripcion = models.TextField(max_length=1000,
                                   help_text='Escribe la descripcion de este libro que se vera en la pagina de inicio...')
    portada = models.ImageField(upload_to='images/', verbose_name="Portada para la pagina",
                                help_text='Ingresa una imagen')

    def portada_tag(self):
        """Para mostrar imagenes en el panel de administracion"""
        return mark_safe('<img src="%s" width="150" />' % (settings.MEDIA_URL + self.portada.name))

    archivo = models.FileField(upload_to='pdf/', verbose_name="Archivo PDF",
                               help_text='Ingresa un archivo PDF.')

    def __str__(self):
        """String que representa el servicio"""
        return self.titulo


class GrupoDeEnlace(models.Model):
    """Modelo representando las agrupaciones de enlaces"""
    posicion = models.PositiveSmallIntegerField()
    grupo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Grupo de enlace'
        verbose_name_plural = 'Grupos de enlaces'

    def __str__(self):
        """String que representa el servicio"""
        return self.grupo


class Enlace(models.Model):
    """Modelo representando los enlaces a mostrar en la pagina de inicio"""
    nombre = models.CharField(max_length=200)
    enlace_externo = models.CharField(max_length=200)
    grupo_de_enlace = models.ForeignKey(
        'GrupoDeEnlace', on_delete=models.CASCADE)

    def enlace_tag(self):
        """Para mostrar enlaces en el panel de administracion"""
        return mark_safe('<a href="%s"/>%s</a>' % (self.enlace_externo, self.enlace_externo))

    def __str__(self):
        """String que representa el servicio"""
        return self.nombre


class Entidad(models.Model):
    """Modelo representando los enlaces a mostrar en la pagina de inicio"""
    nombre = models.CharField(max_length=200)
    enlace_externo = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/', verbose_name="Logo de la entidad",
                             help_text='Ingresa una imagen')

    def enlace_tag(self):
        """Para mostrar enlaces en el panel de administracion"""
        return mark_safe('<a href="%s"/>%s</a>' % (self.enlace_externo, self.enlace_externo))

    def image_tag(self):
        """Para mostrar imagenes en el panel de administracion"""
        return mark_safe('<img src="%s" width="150" />' % (settings.MEDIA_URL + self.logo.name))

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        """String que representa el servicio"""
        return self.nombre


class RedSocial(models.Model):
    """Modelo para una red social y su logo"""
    nombre = models.CharField(max_length=15,
                              help_text="Ingreas el nombre de una red social. Ej: Facebook")
    icono = models.FileField(upload_to='images/', verbose_name="Icono de la RED SOCIAL",
                             help_text='Ingresa una imagen formato SVG')

    class Meta:
        verbose_name = 'Tipo de Red Social'
        verbose_name_plural = 'Tipos de Redes Sociales'

    def __str__(self):
        """String que representa el servicio"""
        return self.nombre


class RedSocialEnlace(models.Model):
    """Modelo representando los enlaces de las redes Sociales"""
    enlace = models.CharField(max_length=100)
    red = models.ForeignKey('RedSocial', on_delete=models.CASCADE,
                            help_text='Elige la red social que quieres editar')

    INSTITUCIONES = (
        ('viceministerio', 'Viceministerio'),
        ('ministerio', 'Ministerio'),
    )

    institucion = models.CharField(
        max_length=15,
        choices=INSTITUCIONES,
        default='viceministerio',
        help_text='Elige la instucion',
    )

    def enlace_tag(self):
        """Para mostrar enlaces en el panel de administracion"""
        return mark_safe('<a href="%s"/>%s</a>' % (self.enlace, self.enlace))

    class Meta:
        verbose_name = 'Enlace de Red Social'
        verbose_name_plural = 'Enlaces de Redes Sociales'

    def __str__(self):
        """String que representa el servicio"""
        return f'{self.red} de {self.get_institucion_display()}'


class NoticiaImportante(models.Model):
    """Modelo de la noticia principal"""
    nombre = models.CharField(max_length=200)
    enlace = models.CharField(max_length=200,
                              help_text="Ingresa el enlace relevante de la noticia")
    banner = models.FileField(upload_to='images/', verbose_name="IMAGEN BANNER",
                              help_text='Ingresa el banner de la noticia')

    def banner_tag(self):
        """Para mostrar imagenes en el panel de administracion"""
        return mark_safe('<img src="%s" width="150" />' % (settings.MEDIA_URL + self.banner.name))

    class Meta:
        verbose_name = 'Noticia Importante'
        verbose_name_plural = 'Noticias Importantes'

    def __str__(self):
        """String que representa el servicio"""
        return self.nombre
