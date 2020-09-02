from django.views import generic
from inicio.models import Servicio, Libro, GrupoDeEnlace, Enlace, Entidad, NoticiaImportante

# VISTAS
# TDOO: INTENTAR SOLUCIONAR https://stackoverflow.com/questions/45135263/class-has-no-objects-member


class IndexListView(generic.ListView):
    """Vista para renderizar la pagina de Inicio"""
    context_object_name = 'index'
    template_name = 'index.html'
    queryset = Servicio.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['servicios'] = self.queryset
        context['libros'] = Libro.objects.all()
        context['grupo_de_enlaces'] = GrupoDeEnlace.objects.all()
        context['enlaces'] = Enlace.objects.all()
        context['entidades'] = Entidad.objects.all()
        context['noticia'] = NoticiaImportante.objects.first()
        return context
