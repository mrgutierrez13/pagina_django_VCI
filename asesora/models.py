from django.db import models
# CONSEJO: Automatic creation date for Django model form objects?
# https://stackoverflow.com/questions/3429878/automatic-creation-date-for-django-model-form-objects

class ContactoAsesora(models.Model):
    """Modelo para los usuarios que necesitan ayuda"""
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    mensaje = models.TextField(max_length=1000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    email_enviado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'VCI TE ASESORA'
        verbose_name_plural = 'SISTEMA VCI TE ASESORA'

    def __str__(self):
        """String que representa el contacto"""
        return self.nombre
