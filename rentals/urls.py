from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('type/<int:car_type_id>/', views.filter_cars, name="filter_cars"),
    path('inventory/', views.inventory_list, name='inventory-list'),
    path('detail/<int:car_id>/', views.car_detail, name='car-detail'),
    path('about/', views.about, name='about'),
    path('search/', views.search_view, name='search'),
]
