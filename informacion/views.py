from django.shortcuts import render
from django.views import generic
from informacion.models import Boletin, Norma, TipoNorma, Fideicomiso, Evento
from inicio.models import Libro

# VISTAS
# TDOO: INTENTAR SOLUCIONAR https://stackoverflow.com/questions/45135263/class-has-no-objects-member


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
    guia = Libro.objects.filter(titulo='GUIA PARA LA EXPORTACIÓN')

    context = {
        'guia': guia
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
