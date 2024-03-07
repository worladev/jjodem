from django.contrib import admin
from .models import CarType, BrandModel, RentalDetails, ServiceReview

# Register your models here.
admin.site.register(CarType)
admin.site.register(BrandModel)
admin.site.register(RentalDetails)
admin.site.register(ServiceReview)
