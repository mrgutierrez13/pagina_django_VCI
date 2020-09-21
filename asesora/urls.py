from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views


#class ResponderEmail(admin.AdminSite):
#    def get_urls(self):
#        urls = super(ResponderEmail, self).get_urls()
#        custom_urls = [
#            url('responder/<int:pk>',
#                self.admin_view(views.responder_email), name="responder"),
#        ]
#        return urls + custom_urls


urlpatterns = [
    path('', views.asesora, name='asesora'),
    path('gracias/', views.asesora_gracias, name='asesora_gracias'),
   # path('admin/<int:pk>', admin.site.urls, name='responder'),
]
