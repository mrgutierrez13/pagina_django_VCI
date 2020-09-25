from django.http import HttpResponseRedirect
from django.shortcuts import render
from asesora.forms import ContactoForm

def asesora(request):
    """Para manejar los datos del formulario VCI te Asesora"""
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('gracias/')
    else:
        form = ContactoForm()

    return render(request, 'asesora.html', {'formulario': form})


def asesora_gracias(request):
    """Cuando los datos del VCI asesora fue exitoso"""
    return render(request, 'asesora_gracias.html', {})
