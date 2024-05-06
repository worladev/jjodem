from django.urls import path
from . import views


app_name = 'booking'

urlpatterns = [
    path('<int:car_id>/', views.book_car, name='book-car'),
]