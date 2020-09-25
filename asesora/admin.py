from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.core.mail import BadHeaderError
from django.conf.urls import url
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from asesora.models import ContactoAsesora
from asesora.forms import ResponderForm
from paginaVCI.settings import DEFAULT_FROM_EMAIL


@admin.register(ContactoAsesora)
class ContactoAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador VCI te asesora"""
    list_display = ('nombre', 'mensaje', 'telefono', 'email',
                    'fecha_creacion', 'email_enviado', 'botones'
                    )

    class Media:
        css = {
            'all': ('reemplazo.css',),
        }

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=all):
        return False

    def proceso_responder(self, request, contacto_id):
        """Metodo para procesar el email del contacto"""
        contacto = self.get_object(request, contacto_id)

        if request.method != 'POST':
            form = ResponderForm()

        else:
            form = ResponderForm(request.POST, contacto)
            if form.is_valid():
                try:
                    form.enviar(contacto)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                else:
                    self.message_user(request, 'Exito')
                    contacto.email_enviado = True
                    contacto.save()
                    url_contacto = reverse(
                        'admin:asesora_contactoasesora_changelist',
                        current_app=self.admin_site.name,
                    )
                    return HttpResponseRedirect(url_contacto)
        context = self.admin_site.each_context(request)
        context['opts'] = self.model._meta
        context['form'] = form
        context['contacto'] = contacto
        context['remitente'] = DEFAULT_FROM_EMAIL
        return TemplateResponse(
            request,
            'admin/asesora/responder.html',
            context,
        )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<contacto_id>.+)/responder/$',
                self.admin_site.admin_view(self.proceso_responder),
                name='responder-email',
            ),
        ]
        return custom_urls + urls

    def botones(self, obj):
        """Metodo para mostrar botones en el panel de administracion"""
        url_responder = reverse('admin:responder-email', args=[obj.pk])
        return format_html(
            '<div class="boton"><a href="{}">Responder a <bold>{}</bold></a></div>',
            url_responder, obj.nombre
        )

    botones.short_description = '-----'

