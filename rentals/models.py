from django.db import models


RATING = (
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★')
)


# Create your models here.
class CarType(models.Model):
    type_image = models.ImageField(upload_to='brand/%Y/%m/%d', blank=True)
    type_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'car type'
        verbose_name_plural = 'car types'

    def __str__(self):
        return self.type_name


class BrandModel(models.Model):
    car_image = models.ImageField(upload_to='car/%Y/%m/%d', blank=True)
    model_name = models.CharField(max_length=200)
    type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    number_of_doors = models.PositiveIntegerField()
    number_of_passengers = models.PositiveIntegerField()
    fuel = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    drive_type = models.CharField(max_length=50)
    description = models.TextField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    class Meta:
        ordering = ['type']

    def __str__(self):
        return self.model_name


class ShopInfo(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='car/%Y/%m/%d', blank=True)
    slogan = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


class ServiceReview(models.Model):
    name = models.CharField(max_length=50)
    review = models.TextField(max_length=250, null=True, blank=True)
    service_rating = models.IntegerField(choices=RATING, default=None)
    vehicle_rating = models.IntegerField(choices=RATING, default=None)
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['review_date']
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    def __str__(self):
        return self.name


class SocialHandle(models.Model):
    handle_name = models.CharField(max_length=50)
    handle_url = models.URLField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'handle'
        verbose_name_plural = 'handles'

    def __str__(self):
        return self.handle_name
