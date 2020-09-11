from django.shortcuts import render
from inicio.models import Servicio, Libro, GrupoDeEnlace, Enlace, Entidad, NoticiaImportante

# VISTAS
# TDOO: INTENTAR SOLUCIONAR https://stackoverflow.com/questions/45135263/class-has-no-objects-member

def index(request):
    """Vista para renderizar la pagina principal"""

    context = {
        'servicios': Servicio.objects.all(),
        'libros': Libro.objects.all(),
        'grupo_de_enlaces': GrupoDeEnlace.objects.all(),
        'enlaces': Enlace.objects.all(),
        'entidades': Entidad.objects.all(),
        'noticia': NoticiaImportante.objects.first(),
    }

    return render(request, 'index.html', context=context)
