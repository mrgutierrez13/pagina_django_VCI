from django import forms


class FormularioVciAsesora(forms.Form):
    """Para instanciar el formulario de VCI te Asesora"""
    nombre = forms.CharField(label='Nombre:', max_length=100,
                             error_messages={'required': 'Por favor ingrese su nombre...'})
    email = forms.EmailField(label='Correo Electrónico:',
                             error_messages={'required': 'Por favor ingrese su correo electrónico en un formato valido...'})
    telefono = forms.CharField(max_length=20, required=False,
                               label='Teléfono:')
    mensaje = forms.CharField(label='Consulta:', max_length=1000, widget=forms.Textarea,
                              initial='Escriba su consulta al VCI...',
                              error_messages={'required': 'Sin una consulta no podremos ayudarle...x'})
