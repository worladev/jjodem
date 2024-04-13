from .models import CarModel


def get_similar_cars(car_type, number_of_rec=5):
    cars_of_type = CarModel.objects.filter(type=car_type)
    similar_cars = cars_of_type.exclude(id=car_type.pk)[:number_of_rec]
    return similar_cars