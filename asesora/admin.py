from django.contrib import admin
from django.utils.html import mark_safe
from django.urls import reverse
from asesora.models import ContactoAsesora

# admin.site.register(ContactoAsesora)


@admin.register(ContactoAsesora)
class ContactoAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador VCI te asesora"""
    list_display = ('nombre', 'mensaje', 'telefono', 'email',
                    'fecha_creacion', 'email_enviado', 'botones')

    class Media:
        css = {
            'all': ('reemplazo.css',),
        }

    def has_add_permission(self, request):
        return False

    def botones(self, obj):
        url = ""
        return mark_safe(
            '<a href="%s">Responder a %s</a>' % (url, obj.nombre))

    botones.allow_tags = True
    botones.short_description = '-----'
    change_form_template = 'admin/responder.html'
