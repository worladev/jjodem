from functools import wraps
from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpResponse  #
from .models import CarType, ShopInfo, CarModel, SocialHandle
from .recommender import get_similar_cars
from django.db.models import Q  #
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


# Create your views here.
def add_shop_info(view_info_func):
    @wraps(view_info_func)
    def _wrapped_view(request, *args, **kwargs):
        shop_info = ShopInfo.objects.all()
        social_handle = SocialHandle.objects.all()
        response = view_info_func(request, *args, shop_info=shop_info, social_handle=social_handle, **kwargs)
        if isinstance(response, dict):
            response['shop_info'] = shop_info
            response['social_info'] = social_handle
        return response
    return _wrapped_view


@add_shop_info
def home(request, shop_info, social_handle):
    car_type = CarType.objects.filter(is_available=True)
    context = {
        'car_type': car_type,
        'shop_info': shop_info,
        'social_handle': social_handle,
        }
    return render(request, 'rentals/home.html', context)


@add_shop_info
def filter_cars(request, car_type_id, shop_info, social_handle):
    car_type = CarType.objects.get(pk=car_type_id)
    filter_car = CarModel.objects.filter(type=car_type, is_available=True)
    context = {
        'car_type': car_type,
        'filter_car': filter_car,
        'shop_info': shop_info,
        'social_handle': social_handle,
        }
    return render(request, 'rentals/filter-cars.html', context)


@add_shop_info
def inventory_list(request, shop_info, social_handle):
    car_models = CarModel.objects.filter(is_available=True)
    context = {
        'car_models': car_models,
        'shop_info': shop_info,
        'social_handle': social_handle,
    }
    return render(request, 'rentals/inventory-list.html', context)


@add_shop_info
def car_detail(request, car_id, shop_info, social_handle):
    try:
        car = get_object_or_404(CarModel, pk=car_id)
        similar_cars = get_similar_cars(car.type) # recommendation function call
    except CarModel.DoesNotExist:
        raise Http404('Car not available')
    # exclude the current car from the recommended cars
    similar_cars = [similar_car for similar_car in similar_cars if similar_car.id != car.id]
    context = {
        'car': car,
        'shop_info': shop_info,
        'similar_cars': similar_cars,
        'social_handle': social_handle,
    }
    return render(request, 'rentals/car-detail.html', context)


@add_shop_info
def about(request, shop_info, social_handle):
    context = {
        'shop_info': shop_info,
        'social_handle': social_handle,
    }
    return render(request, 'rentals/about.html', context)


@add_shop_info
def search_view(request, shop_info, social_handle):
    query = None
    safe_query = None
    results = []
    
    if request.method == 'GET':
        query = request.GET.get('search-data')
        if query:
            # sanitize query to prevent SQL injection attacks
            safe_query = query.strip()  # remove leading and trailing whitespaces
            if safe_query:
                # case-insensitive search (stemming and ranking results)
                search_vector = SearchVector('model_name', 'description')
                search_query = SearchQuery(safe_query)  # filter result
                results = CarModel.objects.annotate(
                    search=search_vector,
                    rank=SearchRank(search_vector, search_query)  # order result by relevancy
                ).filter(search=search_query).order_by('-rank')
            else:
                results = []  # empty query
        else:
            results = CarModel.objects.all()  # empty query
    else:
        return HttpResponse("Method Not Allowed", status=405)  # non-GET request
    
    context = {
        'shop_info': shop_info,
        'safe_query': safe_query,
        'results': results,
        'social_handle': social_handle,
    }
    return render(request, 'rentals/search.html', context)
