from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic
from django.db.models import Sum
from informacion.models import Boletin, Norma, TipoNorma, Fideicomiso, Evento, Proveedor, ProveedorActivo
from inicio.models import Libro


# VISTAS
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
        'secciones_normas': TipoNorma.objects.all().order_by('nombre_seccion'),
        'normas': Norma.objects.all().order_by('titulo'),
    }

    return render(request, 'normativa.html', context=context)


def guia_request(request):
    """Vista para mostrar la guia del exportador"""

    context = {
        'guia': Libro.objects.get(id=1)
    }
    # Render the HTML template
    return render(request, 'guia_exportador.html', context=context)



class FideicomisosListView(generic.ListView):
    """Vista para renderizar los fideicomisos"""
    model = Fideicomiso
    context_object_name = 'fideicomisos'
    template_name = 'fideicomisos.html'
    ordering = ["-fecha"]


def eventos(request):
    """Vista para renderizar los eventos"""
    eventos_ferias = Evento.objects.all().order_by('-fecha')
    return render(request, 'eventos.html', {'eventos': eventos_ferias})



def proveedores(request):
    """Vista para mostrar la pagina inicial de proveedores"""
    context = {}
    return render(request, 'proveedores.html', context=context)


def proveedores_contacto(request):
    """Vista para pedir los registros de proveedores"""

    proveedores_completo = Proveedor.objects.select_related('municipio__departamento').order_by('razon_social')
    paginator = Paginator(proveedores_completo, 100)
    numero_pagina = request.GET.get('pag')
    pagina_actual = paginator.get_page(numero_pagina)

    return render(request, 'proveedores_contacto.html', {'pagina_actual': pagina_actual})


def proveedores_empresas(request):
    """Vista para los datos de las empresas y sus actividades"""

    #lista_empresa_producto = ActividadEconomica.objects.select_related('nit_ci', 'nandina').distinct()


    proveedores_activos = ProveedorActivo.objects.annotate(kg_bruto=Sum('actividadeconomica__kg_bruto'),
                                                           kg_neto=Sum(
                                                               'actividadeconomica__kg_neto'),
                                                           cif=Sum('actividadeconomica__cif')).order_by('razon_social')
    paginator = Paginator(proveedores_activos, 100)
    numero_pagina = request.GET.get('pag')
    pagina_actual = paginator.get_page(numero_pagina)

    context = {
        'pagina_actual': pagina_actual,
        #'productos': lista_empresa_producto,
    }

    return render(request, 'proveedores_empresas.html', context=context)

def brokers(request):
    """Vista para mostrar los brokers"""
    context = {}
    return render(request, 'brokers.html', context=context)
