from django.urls import path
from . import views

urlpatterns = [
    path('guia/', views.guia_request, name='guia'),
    path('boletines/', views.BoletinListView.as_view(), name='boletines'),
    path('normativa/', views.normativa, name='normativa'),
    path('fideicomisos/', views.FideicomisosListView.as_view(), name='fideicomisos'),
    path('brokers/', views.brokers, name='brokers'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('proveedores/contacto/', views.proveedores_contacto, name='proveedores_contacto'),
    path('proveedores/empresas/', views.proveedores_empresas, name='proveedores_empresas'),
    path('videos/', views.videos, name='videos'),
    path('eventos/', views.EventosListView.as_view(), name='eventos'),
]
