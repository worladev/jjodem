from functools import wraps
from django.shortcuts import render, Http404, get_object_or_404
from .models import CarType, ShopInfo, CarModel
from .recommender import get_similar_cars


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
    car_type = CarType.objects.filter(is_available=True)
    context = {
        'car_type': car_type,
        'shop_info': shop_info,
        }
    return render(request, 'rentals/home.html', context)


@add_shop_info
def filter_cars(request, car_type_id, shop_info):
    car_type = CarType.objects.get(pk=car_type_id)
    filter_car = CarModel.objects.filter(type=car_type, is_available=True)
    context = {
        'car_type': car_type,
        'filter_car': filter_car,
        'shop_info': shop_info,
        }
    return render(request, 'rentals/filter-cars.html', context)


@add_shop_info
def inventory_list(request, shop_info):
    car_models = CarModel.objects.filter(is_available=True)
    context = {
        'car_models': car_models,
        'shop_info': shop_info,
    }
    return render(request, 'rentals/inventory-list.html', context)


@add_shop_info
def car_detail(request, car_id, shop_info):
    try:
        car = get_object_or_404(CarModel, pk=car_id)
        similar_cars = get_similar_cars(car.type)
    except CarModel.DoesNotExist:
        raise Http404('Car not available')
    
    similar_cars = [similar_car for similar_car in similar_cars if similar_car.id != car.id]
    context = {
        'car': car,
        'shop_info': shop_info,
        'similar_cars': similar_cars,
    }
    return render(request, 'rentals/car-detail.html', context)


@add_shop_info
def about(request, shop_info):
    context = {
        'shop_info': shop_info
    }
    return render(request, 'rentals/about.html', context)
