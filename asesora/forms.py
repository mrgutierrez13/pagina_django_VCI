from django import forms
#from django.utils.translation import gettext_lazy as _
from .models import ContactoAsesora


class ContactoForm(forms.ModelForm):
    """Formulario basado en clases"""
    nombre = forms.CharField(label='Nombre*', max_length=100, min_length=3)
    email = forms.EmailField(label='Correo Electrónico*')
    telefono = forms.CharField(max_length=20, min_length=7, required=False,
                               label='Teléfono/Celular')
    mensaje = forms.CharField(label='Mensaje de consulta*',
                              max_length=1000, min_length=10,
                              widget=forms.Textarea(attrs={'placeholder': 'Ingrese su mensaje para el VCI...'}))

    class Meta:
        model = ContactoAsesora
        fields = ('nombre', 'email', 'telefono', 'mensaje')

# TODO: CREAR BOTONES Y ENVIAR EMAIL
# https://hakibenita.com/how-to-add-custom-action-buttons-to-django-admin
