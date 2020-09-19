from django.urls import path
from . import views

urlpatterns = [
    path('', views.tramites, name='tramites'),
    path('sprocon/', views.sprocon_request, name='sprocon'),
    path('ritex/', views.sprocon_request, name='ritex'),
]
