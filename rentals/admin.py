from django.contrib import admin
from .models import CarType, BrandModel, ShopInfo, ServiceReview, SocialHandle

# Register your models here.
admin.site.register(CarType)

admin.site.register(BrandModel)

admin.site.register(ShopInfo)

admin.site.register(ServiceReview)

admin.site.register(SocialHandle)
