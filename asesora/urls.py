from django.urls import path
from . import views

urlpatterns = [
    path('', views.asesora, name='asesora'),
]
