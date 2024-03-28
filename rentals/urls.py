from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('/<str:type_name>/', views.filter, name="filter")
]
