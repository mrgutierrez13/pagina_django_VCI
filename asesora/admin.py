from django.contrib import admin
from asesora.models import ContactoAsesora

# admin.site.register(ContactoAsesora)


@admin.register(ContactoAsesora)
class ContactoAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador VCI te asesora"""
    list_display = ('nombre', 'mensaje', 'telefono', 'email', 'fecha_creacion', 'email_enviado',)
    class Media:
        css = {
            'all': ('reemplazo.css',),
        }
    def has_add_permission(self, request):
        return False


