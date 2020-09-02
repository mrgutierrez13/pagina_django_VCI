from django.contrib import admin
from .models import Boletin, Norma, TipoNorma, Fideicomiso, Evento, Proveedor, Municipio

admin.site.register(Boletin)
admin.site.register(Norma)
admin.site.register(TipoNorma)
admin.site.register(Fideicomiso)
admin.site.register(Evento)
admin.site.register(Proveedor)
admin.site.register(Municipio)

