from django.shortcuts import render
from .models import CarType, ShopInfo


# Create your views here.
def home(request):
    car_type = CarType.objects.all()
    shop_info = ShopInfo.objects.all()
    context = {
        'car_type': car_type,
        'shop_info': shop_info,
        }
    return render(request, 'rentals/home.html', context)
# checkout django template inheritance
