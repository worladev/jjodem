from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('type/<int:car_type_id>/', views.filter_cars, name="filter_cars")
]
