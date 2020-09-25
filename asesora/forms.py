from django import forms
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from .models import ContactoAsesora

ACERCA = 'Mensaje de respuesta del VCI'


class ContactoForm(forms.ModelForm):
    """Formulario basado en clases"""
    nombre = forms.CharField(label='Nombre*', max_length=100, min_length=3)
    email = forms.EmailField(label='Correo Electrónico*')
    telefono = forms.CharField(max_length=20, min_length=7, required=False,
                               label='Teléfono/Celular')
    mensaje = forms.CharField(label='Mensaje de consulta*',
                              max_length=1000, min_length=10,
                              widget=forms.Textarea(
                                  attrs={
                                      'placeholder': 'Ingrese su mensaje para el VCI...'}
                              )
                              )

    class Meta:
        model = ContactoAsesora
        fields = ('nombre', 'email', 'telefono', 'mensaje')


class ResponderForm(forms.Form):
    """Formulario basado en clases"""

    tema = forms.CharField(label='Tema',
                           max_length=200,
                           min_length=5,
                           initial=ACERCA,
                           widget=forms.TextInput(attrs={'size': '80'})
                           )

    mensaje = forms.CharField(label='Respuesta',
                              max_length=1000, min_length=10,
                              widget=forms.Textarea(
                                  attrs={
                                      'cols': '80'}
                              )
                              )

    def enviar(self, contacto):
        """Metodo para enviar email al contacto"""
        tema = self.cleaned_data['tema']
        remitente = None  # automaticamente utiliza DEFAULT_FROM_EMAIL
        destinatario = [contacto.email]
        mensaje = self.cleaned_data['mensaje']
        try:
            send_mail(tema, mensaje, remitente, destinatario)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

