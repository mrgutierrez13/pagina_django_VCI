from django.contrib import admin
from inicio.models import *

admin.site.register(Servicio)
admin.site.register(Libro)
admin.site.register(GrupoDeEnlace)
admin.site.register(Enlace)
admin.site.register(Entidad)
admin.site.register(RedSocialEnlace)
admin.site.register(RedSocial)
admin.site.register(NoticiaImportante)



admin.site.site_title = "Pagina del VCI"
admin.site.site_header = "Administracion de la pagina del Viceministerio de Comercio Interno"
admin.site.index_title = "Panel de administracion"
