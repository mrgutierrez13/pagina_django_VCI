from django.urls import path
from . import views

urlpatterns = [
    path('', views.en_desarrollo, name='en_desarrollo'),
]
