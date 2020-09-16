from django.urls import path
from . import views

urlpatterns = [
    path('', views.asesora, name='asesora'),
    path('gracias/', views.asesora_gracias, name='asesora_gracias'),
]
