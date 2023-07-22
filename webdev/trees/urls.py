from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('tree_type_list/', views.tree_type_list, name='tree_type_list'),
    path('tree_type_list/<int:id>', views.tree_type, name='tree_type'),
    path('search/', views.search_result, name='search_result'),
    path('tree_instance_list/', views.tree_instance_list, name='tree_instance_list'),
    path('tree_instance_list/<int:id>', views.tree_instance, name='tree_instance'),
    #path('admin_anders/', views.admin_anders, name='admin_anders'),
]