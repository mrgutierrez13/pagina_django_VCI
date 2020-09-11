from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic
from informacion.models import Boletin, Norma, TipoNorma, Fideicomiso, Evento, Proveedor
from inicio.models import Libro

# VISTAS
# TODO: INTENTAR SOLUCIONAR https://stackoverflow.com/questions/45135263/class-has-no-objects-member
# CONSEJO: INNER JOIN, REVERSE LOOKUP GRANDPARENT TABLE
# https://docs.djangoproject.com/en/2.2/ref/models/querysets/#select-related


class BoletinListView(generic.ListView):
    """Vista para renderizar la informacion sobre boletines"""
    model = Boletin
    context_object_name = 'boletines'
    template_name = 'boletines.html'


class NormativaListView(generic.ListView):
    """Vista para mostrar las normas"""
    context_object_name = 'normativa'
    template_name = 'normativa.html'
    queryset = TipoNorma.objects.all()

    def get_context_data(self, **kwargs):
        context = super(NormativaListView, self).get_context_data(**kwargs)
        context['secciones_normas'] = self.queryset
        context['normas'] = Norma.objects.all()
        return context


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
    """Vista para pedir los registros de proveedores"""

    proveedores_completo = Proveedor.objects.select_related('municipio__departamento')
    paginator = Paginator(proveedores_completo, 100)
    numero_pagina = request.GET.get('page')
    pagina_actual = paginator.get_page(numero_pagina)

    return render(request, 'proveedores.html', {'pagina_actual': pagina_actual})
