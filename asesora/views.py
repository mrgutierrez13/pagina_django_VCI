from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import FormularioVciAsesora


def asesora(request):
    """Para manejar los datos del formulario VCI te Asesora"""
    if request.method == 'POST':
        form = FormularioVciAsesora(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/gracias/')
    else:
        form = FormularioVciAsesora()

    return render(request, 'asesora.html', {'formulario': form})
