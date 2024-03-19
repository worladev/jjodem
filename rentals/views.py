from django.shortcuts import render
from .models import CarType


# Create your views here.
def home(request):
    car_type = CarType.objects.all()
    context = {'car_type':car_type}
    return render(request, 'rentals/home.html', context)


    # checkout django template inheritance
