from functools import wraps
from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpResponse  #
from .models import CarType, ShopInfo, CarModel, SocialHandle
from .recommender import get_similar_cars
from django.db.models import Q  #
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


# HOME VIEW
def home(request):
    car_type = CarType.objects.filter(is_available=True)
    context = {
        'car_type': car_type,
        }
    return render(request, 'rentals/home.html', context)


# FILTER CARS VIEW
def filter_cars(request, car_type_id):
    car_type = CarType.objects.get(pk=car_type_id)
    filter_car = CarModel.objects.filter(type=car_type, is_available=True)
    context = {
        'car_type': car_type,
        'filter_car': filter_car,
        }
    return render(request, 'rentals/filter-cars.html', context)


# ALL INVENTORY LIST VIEW
def inventory_list(request):
    car_models = CarModel.objects.filter(is_available=True)
    context = {
        'car_models': car_models,
    }
    return render(request, 'rentals/inventory-list.html', context)


# CAR DETAIL VIEW
def car_detail(request, car_id):
    car = CarModel.objects.all(pk=car_id)
    similar_cars = get_similar_cars(car.type) # recommendation function call
    # exclude the current car from the recommended cars
    similar_cars = [similar_car for similar_car in similar_cars if similar_car.id != car.id]
    context = {
        'car': car,
        'similar_cars': similar_cars,
    }
    return render(request, 'rentals/car-detail.html', context)


# ABOUT VIEW
def about(request):
    return render(request, 'rentals/about.html')


# DATA SEARCH VIEW
def search_view(request):
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
        'safe_query': safe_query,
        'results': results,
    }
    return render(request, 'rentals/search.html', context)


# TERMS AND PRIVACY POLICY VIEW
def terms_and_conditon_privacy(request):
    return render(request, 'rentals/t-and-c-privacy.html')


# CUSTOM 404 ERROR PAGE VIEW
def not_found_view(request):
    return render(request, '404.html', status=404)
