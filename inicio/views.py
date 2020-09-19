from django.shortcuts import render
from inicio.models import Servicio, Libro, GrupoDeEnlace, Enlace, Entidad, NoticiaImportante

# VISTAS
# TDOO: INTENTAR SOLUCIONAR https://stackoverflow.com/questions/45135263/class-has-no-objects-member


def index(request):
    """Vista para renderizar la pagina principal"""

    context = {
        'servicios': Servicio.objects.all().order_by('posicion'),
        'libros': Libro.objects.all().order_by('posicion'),
        'grupo_de_enlaces': GrupoDeEnlace.objects.all().order_by('posicion'),
        'enlaces': Enlace.objects.all().order_by('nombre'),
        'entidades': Entidad.objects.all().order_by('nombre'),
        'noticia': NoticiaImportante.objects.first(),
    }

    return render(request, 'index.html', context=context)
