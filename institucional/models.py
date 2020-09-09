from django.db import models

# Create your models here.
# SOLUCION ERROR PARA BARRA BAJA '_'
# https://stackoverflow.com/questions/12995888/name-is-not-defined/12995923
# CONSEJO: Para sacar el 'human readable text'
# https://stackoverflow.com/questions/47881817/the-human-readable-value-of-the-field-choices-in-django
# TODO:  Limit number of model instances to be created - django
# https://stackoverflow.com/questions/2138408/limit-number-of-model-instances-to-be-created-django


class Texto(models.Model):
    """Modelo representando el texto a desplegar en la pagina institucional"""
    contenido = models.TextField(max_length=1000,
                                 help_text='El texto aparecera tal cual en la pagina')

    SECCIONES = (
        ('qui', "¿Quienes Somos?"),
        ('mis', "Mision"),
        ('obj', "Objetivos"),
        ('org', "Organización"),
    )

    seccion = models.CharField(
        max_length=3,
        choices=SECCIONES,
        default='qui',
        help_text='Selecciona la sección de este texto',
    )

    def __str__(self):
        """String que representa el servicio"""
        return self.get_seccion_display()


class FuncionarioPublico(models.Model):
    """Modelo representando la informacion de un funcionario publico en la pagina Institucional"""
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

    foto = models.FileField(upload_to='images/', verbose_name="",
                            help_text='Ingresa una foto del funcionario publico')
    class Meta:
        verbose_name = 'Funcionario Público'
        verbose_name_plural = 'Funcionarios Públicos'

    def __str__(self):
        """String que representa el servicio"""
        return self.nombre_completo
