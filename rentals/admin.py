from django.contrib import admin
from .models import CarType, CarModel, ShopInfo, ServiceReview, SocialHandle

# Register your models here.
admin.site.register(CarType)

admin.site.register(CarModel)

admin.site.register(ShopInfo)

admin.site.register(ServiceReview)

admin.site.register(SocialHandle)
