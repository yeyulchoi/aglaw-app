from django.urls import path
from . import views

urlpatterns = [
    path('', views.deals, name='deals'),
    path('<int:deal_id>',views.deal_detail, name='deal_detail'),
    path('search', views.search, name='search')
]