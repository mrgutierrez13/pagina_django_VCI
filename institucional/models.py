from django.db import models
from django.utils.html import mark_safe
from django.conf import settings


class SeccionTexto(models.Model):
    """Modelo representando el texto a desplegar en la pagina institucional"""
    posicion = models.PositiveSmallIntegerField()
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(max_length=1000,
                                 help_text='El texto aparecera tal cual en la pagina')

    def __str__(self):
        """String que representa el servicio"""
        return self.titulo


class FuncionarioPublico(models.Model):
    """Modelo representando la informacion de un funcionario publico en la pagina Institucional"""
    posicion = models.PositiveSmallIntegerField()
    nombre_completo = models.CharField(max_length=200,
                                       help_text='El nombre que aparecera tal cual en la pagina')
    cargo = models.CharField(max_length=200, default='miembro',
                             help_text='El cargo aparecera tal cual en la pagina')
    NIVELES = (
        ('N1', "NIVEL 1"),
        ('N2', "NIVEL 2"),
        ('N3', "NIVEL 3"),
    )

    nivel = models.CharField(
        max_length=2,
        choices=NIVELES,
        default='N3',
        help_text='Selecciona el nivel en que se ubicara en la pagina',
    )

    foto = models.FileField(upload_to='images/', verbose_name="FOTO DEL FUNCIONARIO",
                            help_text='Ingresa una foto del funcionario publico')

    def foto_tag(self):
        """Para mostrar imagenes en el panel de administracion"""
        return mark_safe('<img src="%s" width="150" />' % (settings.MEDIA_URL + self.foto.name))

    class Meta:
        verbose_name = 'Funcionario Público'
        verbose_name_plural = 'Funcionarios Públicos'

    def __str__(self):
        """String que representa el servicio"""
        return self.nombre_completo
