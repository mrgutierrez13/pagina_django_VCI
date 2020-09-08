from django.db import models
from colorfield.fields import ColorField

# Modelos

# TODO: VALIDACION SVG
# https://stackoverflow.com/questions/38006200/allow-svg-files-to-be-uploaded-to-imagefield-via-django-admin
# CONSEJO: MANEJAR DATABASE DE IMAGENES
# https://www.learningaboutelectronics.com/Articles/How-to-insert-images-into-a-database-table-with-Python-in-Django.php
# CONSEJO: CUANDO LAS MIGRACIONES NO FUNCIONAN  python manage.py migrate --run-syncdb
# https://stackoverflow.com/questions/12784835/django-no-such-table/47408979
# CONSEJO: PARA AGREGAR COLOR-PICKER A LA BANDEJA ADMIN:  django-colorfield
# CONSEJO: EDITAR SQLITE DATABASE
# https://www.dev2qa.com/how-to-drop-change-tables-from-sqlite3-database-in-django/
# CONSEJO: As long as the apps are in INSTALLED_APPS
# and the template loader for apps dirs is enabled,
# you can include any template from another app
# https://stackoverflow.com/questions/4571686/django-include-template-from-another-app
# CONSEJO: Para borrar fotos/media inutilizadas en el proyecto: pip install django-cleanup
# https://stackoverflow.com/questions/21941503/django-delete-unused-media-files


class Servicio(models.Model):
    """Modelo representando la informacion de un servicio a ser mostrado en la pagina de inicio"""
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200,
                                   help_text='Escribe la descripcion del servicio que se vera en la pagina de inicio...')
    icono = models.FileField(upload_to='images/',
                             verbose_name="", help_text='Ingresa una imagen formato SVG')

    def __str__(self):
        """String que representa el servicio"""
        return self.nombre


class Libro(models.Model):
    """Modelo de un libro importante para mostrar en la pagina de inicio"""
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')
    descripcion = models.TextField(max_length=1000,
                                   help_text='Escribe la descripcion de este libro que se vera en la pagina de inicio...')
    portada = models.ImageField(
        upload_to='images/', verbose_name="", help_text='Ingresa una imagen')

    archivo = models.FileField(
        upload_to='pdf/', verbose_name="", help_text='Ingresa un archivo PDF.')

    def __str__(self):
        """String que representa el servicio"""
        return self.titulo


class GrupoDeEnlace(models.Model):
    """Modelo representando las agrupaciones de enlaces"""
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

    def __str__(self):
        """String que representa el servicio"""
        return self.nombre


class Entidad(models.Model):
    """Modelo representando los enlaces a mostrar en la pagina de inicio"""
    nombre = models.CharField(max_length=200)
    enlace_externo = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/', 
                             verbose_name="", help_text='Ingresa una imagen')

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
    icono = models.FileField(upload_to='images/', 
                             verbose_name="", help_text='Ingresa una imagen formato SVG')

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
    banner = models.FileField(upload_to='images/', verbose_name="",
                              help_text='Ingresa el banner de la noticia')

    class Meta:
        verbose_name = 'Noticia Importante'
        verbose_name_plural = 'Noticias Importantes'

    def __str__(self):
        """String que representa el servicio"""
        return self.nombre
