from django.shortcuts import render
from .models import FuncionarioPublico, Texto

# VISTAS


def institucional(request):
    """Vista para renderizar la pagina institucional"""

    context = {
        'quienes': Texto.objects.get(seccion='qui'),
        'mision': Texto.objects.get(seccion='mis'),
        'objetivos': Texto.objects.get(seccion='obj'),
        'organizacion': Texto.objects.get(seccion='org'),
        'funcionarios1': FuncionarioPublico.objects.filter(nivel='N1'),
        'funcionarios2': FuncionarioPublico.objects.filter(nivel='N2'),
        'funcionarios3': FuncionarioPublico.objects.filter(nivel='N3'),
    }

    return render(request, 'institucional.html', context=context)
