from django.contrib import admin
from .models import Boletin, Norma, TipoNorma, Fideicomiso, Evento

admin.site.register(TipoNorma)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de los eventos"""
    list_display = ('nombre', 'enlace', 'descripcion', 'fecha',)
    ordering = ('-fecha',)


@admin.register(Boletin)
class BoletinAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de los boletines"""
    list_display = ('titulo', 'portada_tag', 'archivo',)
    ordering = ('titulo',)

@admin.register(Norma)
class NormaAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de las normas"""
    list_display = ('titulo', 'numero', 'fecha', 'descripcion', 'seccion_de_norma')
    ordering = ('seccion_de_norma', 'titulo',)

@admin.register(Fideicomiso)
class FideicomisoAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de los fideicomisos"""
    list_display = ('nombre', 'decreto_descripcion', 'fecha',)
    ordering = ('fecha',)
