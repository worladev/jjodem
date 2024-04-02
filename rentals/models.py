from django.db import models


# Create your models here.
class CarType(models.Model):
    type_image = models.ImageField(upload_to='type/%Y/%m/%d', blank=True)
    type_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'car type'
        verbose_name_plural = 'car types'

    def __str__(self):
        return self.type_name


class CarModel(models.Model):
    FUEL = [
        ('Gasoline', 'Gasoline'),
        ('Diesel', 'Diesel'),
        ('Bio-diesel', 'Bio-diesel'),
        ('Ethanol', 'Ethanol'),
    ]
    TRANSMISSION = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]
    DRIVE_TYPE = [
        ('AWD', 'all-wheel'),
        ('FWD', 'front-wheel'),
        ('RWD', 'rear-wheel'),
        ('4WD', '4-wheel'),
    ]
    type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=200)
    model_image = models.ImageField(upload_to='car/%Y/%m/%d', blank=True)
    number_of_doors = models.PositiveIntegerField()
    number_of_passengers = models.PositiveIntegerField()
    fuel = models.CharField(choices=FUEL, max_length=50, default=None)
    transmission = models.CharField(choices=TRANSMISSION, max_length=50, default=None)
    drive_type = models.CharField(choices=DRIVE_TYPE, max_length=50, default=None)
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
    RATING = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★')
    ]
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
