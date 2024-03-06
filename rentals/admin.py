from django.contrib import admin
from .models import CarBrand, BrandModel, RentalDetails

# Register your models here.
admin.site.register(CarBrand)
admin.site.register(BrandModel)
admin.site.register(RentalDetails)
