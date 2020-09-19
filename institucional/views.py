from django.shortcuts import render
from .models import FuncionarioPublico, SeccionTexto

# VISTAS


def institucional(request):
    """Vista para renderizar la pagina institucional"""

    context = {
        'textos': SeccionTexto.objects.all().order_by('posicion'),
        'funcionarios1': FuncionarioPublico.objects.filter(nivel='N1').order_by('posicion'),
        'funcionarios2': FuncionarioPublico.objects.filter(nivel='N2').order_by('posicion'),
        'funcionarios3': FuncionarioPublico.objects.filter(nivel='N3').order_by('posicion'),
    }

    return render(request, 'institucional.html', context=context)
