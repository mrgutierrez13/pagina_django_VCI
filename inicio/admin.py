from django.contrib import admin
from inicio.models import RedSocial, RedSocialEnlace, Servicio, Enlace,\
                          Entidad, GrupoDeEnlace, Libro, NoticiaImportante

admin.site.register(RedSocial)

MAX_SERVICIOS = 5


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de Servicios"""
    list_display = ('nombre', 'enlace', 'descripcion', 'icono_tag', 'posicion')
    ordering = ('posicion',)

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_SERVICIOS:
            return False
        return super().has_add_permission(request)


@admin.register(Enlace)
class EnlaceAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de enlaces"""
    list_display = ('nombre', 'enlace_tag', 'grupo_de_enlace',)
    ordering = ('grupo_de_enlace', 'nombre',)


@admin.register(GrupoDeEnlace)
class GrupoDeEnlaceAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de enlaces"""
    list_display = ('grupo', 'posicion',)
    ordering = ('posicion',)


@admin.register(RedSocialEnlace)
class RedSocialAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de enlaces de redes sociales"""
    list_display = ('red', 'institucion', 'enlace_tag')
    ordering = ('institucion', 'red',)


@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de enlaces de las entidades"""
    list_display = ('nombre', 'enlace_tag', 'image_tag',)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de los libros en la pagina inicial"""
    list_display = ('titulo', 'descripcion', 'portada_tag', 'posicion',)
    ordering = ('posicion',)


MAX_NOTICIA = 1


@admin.register(NoticiaImportante)
class NoticiaImportanteAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de la Noticia importante"""
    list_display = ('nombre', 'enlace', 'banner_tag',)

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_NOTICIA:
            return False
        return super().has_add_permission(request)


admin.site.site_title = "Pagina del VCI"
admin.site.site_header = "Administracion de la pagina del Viceministerio de Comercio Interno"
admin.site.index_title = "Panel de administracion"
