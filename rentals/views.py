from functools import wraps
from django.shortcuts import render
from .models import CarType, ShopInfo, CarModel


# Create your views here.
def add_shop_info(view_info_func):
    @wraps(view_info_func)
    def _wrapped_view(request, *args, **kwargs):
        shop_info = ShopInfo.objects.all()
        response = view_info_func(request, *args, shop_info=shop_info, **kwargs)
        if isinstance(response, dict):
            response['shop_info'] = shop_info
        return response
    return _wrapped_view


@add_shop_info
def home(request, shop_info):
    car_type = CarType.objects.all()
    context = {
        'car_type': car_type,
        'shop_info': shop_info,
        }
    return render(request, 'rentals/home.html', context)


@add_shop_info
def filter_cars(request, car_type_id, shop_info):
    car_type = CarType.objects.get(pk=car_type_id)
    filter_car = CarModel.objects.filter(type=car_type)
    context = {
        'car_type': car_type,
        'filter_car': filter_car,
        'shop_info': shop_info,
        }
    return render(request, 'rentals/filter-cars.html', context)
    