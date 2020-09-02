from django.urls import path
from . import views

urlpatterns = [
    path('guia/', views.guia_request, name='guia'),
    path('boletines/', views.BoletinListView.as_view(), name='boletines'),
    path('normativa/', views.NormativaListView.as_view(), name='normativa'),
    #path('publicaciones/', views.PublicacionesListView.as_view(), name='publicaciones'),
    path('sprocon/', views.sprocon_request, name='sprocon'),
    path('fideicomisos/', views.FideicomisosListView.as_view(), name='fideicomisos'),
    #path('brokers/', views.BrokersListView.as_view(), name='brokers'),
    #path('proveedores/', views.ProveedoresListView.as_view(), name='proveedores'),
    #path('videos/', views.VideosListView.as_view(), name='videos'),
    path('eventos/', views.EventosListView.as_view(), name='eventos'),
]
