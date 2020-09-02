from django.views import generic
from .models import FuncionarioPublico, Texto

# VISTAS

class InstitucionalListView(generic.ListView):
    """Vista para renderizar la pagina institucional"""
    context_object_name = 'institucional'
    template_name = 'institucional.html'
    queryset = Texto.objects.all()

    def get_context_data(self, **kwargs):
        context = super(InstitucionalListView, self).get_context_data(**kwargs)
        context['textos'] = self.queryset
        funcionarios_nivel1 = FuncionarioPublico.objects.filter(nivel='N1')
        funcionarios_nivel2 = FuncionarioPublico.objects.filter(nivel='N2')
        funcionarios_nivel3 = FuncionarioPublico.objects.filter(nivel='N3')
        context['funcionarios1'] = funcionarios_nivel1
        context['funcionarios2'] = funcionarios_nivel2
        context['funcionarios3'] = funcionarios_nivel3

        return context
