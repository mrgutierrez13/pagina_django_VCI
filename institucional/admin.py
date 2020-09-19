from django.contrib import admin
from .models import FuncionarioPublico, SeccionTexto


@admin.register(SeccionTexto)
class SeccionTextoAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de textos en institucional"""
    list_display = ('titulo', 'contenido', 'posicion',)
    ordering = ('posicion',)


@admin.register(FuncionarioPublico)
class FuncionarioPublicoAdmin(admin.ModelAdmin):
    """Opciones del panel de Administrador de los funcionarios publicos"""
    list_display = ('nombre_completo', 'cargo',
                    'foto_tag', 'nivel', 'posicion',)
    ordering = ('nivel', 'posicion',)
