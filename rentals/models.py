from django.db import models


# Create your models here.
class CarBrand(models.Model):
    brand_image = models.ImageField(upload_to='brand/%Y/%m/%d', blank=True)
    brand_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.brand_name


class BrandModel(models.Model):
    car_image = models.ImageField(upload_to='car/%Y/%m/%d', blank=True)
    model_name = models.CharField(max_length=200)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    number_of_doors = models.PositiveIntegerField()
    number_of_passengers = models.PositiveIntegerField()
    fuel = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    drive_type = models.CharField(max_length=50)
    description = models.TextField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.model_name
