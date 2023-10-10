from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('search/', views.search_result, name='search_result'),
    path('list_art/', views.list_art, name='list_art'),
    path('list_art/<int:id>', views.detail_art, name='detail_art'),
    path('list_planta/', views.list_planta, name='list_planta'),
    path('list_planta/<int:id>', views.detail_planta, name='detail_planta'),
]