from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions, name='transactions'),
    path('<int:file_number>',views.deal_detail, name='deal_detail'),
    path('search', views.search, name='search')
]