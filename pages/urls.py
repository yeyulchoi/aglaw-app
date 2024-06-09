from django.urls import path
from . import views
from django.conf.urls import handler404, handler500, handler403, handler400


urlpatterns = [
    path('', views.home,name='home'),

    path('about', views.about,name='about'),
    path('services', views.services,name='services'),
    path('contact', views.contact,name='contact'),





]