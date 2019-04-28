# mysite_login/urls.py
 
from django.conf.urls import url
from django.contrib import admin
from login import views
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
]