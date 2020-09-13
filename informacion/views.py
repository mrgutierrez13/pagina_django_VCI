from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic
from informacion.models import Boletin, Norma, TipoNorma, Fideicomiso, Evento, Proveedor
from inicio.models import Libro

# VISTAS
# TODO: INTENTAR SOLUCIONAR https://stackoverflow.com/questions/45135263/class-has-no-objects-member
# CONSEJO: INNER JOIN, REVERSE LOOKUP GRANDPARENT TABLE
# https://docs.djangoproject.com/en/2.2/ref/models/querysets/#select-related
# CONSEJO: Para convertir un Queryset a JSON usar Django serializer
# https://stackoverflow.com/questions/15874233/output-django-queryset-as-json

class BoletinListView(generic.ListView):
    """Vista para renderizar la informacion sobre boletines"""
    model = Boletin
    context_object_name = 'boletines'
    template_name = 'boletines.html'


def normativa(request):
    """Vista para renderizar las normas"""

    context = {
        'secciones_normas': TipoNorma.objects.all(),
        'normas': Norma.objects.all(),
    }

    return render(request, 'normativa.html', context=context)

def guia_request(request):
    """Vista para mostrar la guia del exportador"""

    context = {
        'guia': Libro.objects.get(id=1)
    }
    # Render the HTML template
    return render(request, 'guia_exportador.html', context=context)


def sprocon_request(request):
    """Vista para mostrar sprocon"""
    context = {}
    # Render the HTML template
    return render(request, 'sprocon.html', context=context)


class FideicomisosListView(generic.ListView):
    """Vista para renderizar los fideicomisos"""
    model = Fideicomiso
    context_object_name = 'fideicomisos'
    template_name = 'fideicomisos.html'


class EventosListView(generic.ListView):
    """Vista para renderizar los eventos"""
    model = Evento
    context_object_name = 'eventos'
    template_name = 'eventos.html'


def proveedores(request):
    """Vista para mostrar la pagina inicial de proveedores"""
    context = {}
    return render(request, 'proveedores.html', context=context)


def proveedores_contacto(request):
    """Vista para pedir los registros de proveedores"""

    proveedores_completo = Proveedor.objects.select_related('municipio__departamento')
    paginator = Paginator(proveedores_completo, 100)
    numero_pagina = request.GET.get('pag')
    pagina_actual = paginator.get_page(numero_pagina)

    return render(request, 'proveedores_contacto.html', {'pagina_actual': pagina_actual})
