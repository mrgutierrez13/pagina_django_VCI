from django.urls import path
from . import views

urlpatterns = [
    path('', views.InstitucionalListView.as_view(), name='institucional'),
]
