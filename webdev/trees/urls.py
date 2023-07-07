from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('tree_type_list/', views.tree_type, name='tree_type_list'),
    path('tree_type_list/<int:id>', views.tree_wiki, name='tree_type_wiki'),
    path('search/', views.search_result, name='search_result'),
]