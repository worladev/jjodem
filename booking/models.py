from django.conf import settings
from django.db import models
from rentals.models import CarModel
from django.utils import timezone
from account.models import CustomUser


def get_def_model_id():
    default_instance = CustomUser.objects.first()
    if default_instance:
        return default_instance.pk
    return None


# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_def_model_id)
    car_book = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    start_date = models.DateField(db_index=True)
    end_date = models.DateField(db_index=True)
    booking_date = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(default=False)
    
    class Meta:
        indexes = [
            models.Index(fields=['start_date', 'end_date']),
        ]
        ordering = ['-booking_date']
    
    def __str__(self):
        # return f"{self.user.username}'s booking for {self.car_book.model_name}"
        return f"{self.car_book.type.type_name} - {self.car_book.model_name}"
    
    def get_price(self):
        return self.car_book.price
    
    # to retrieve get price for the specific car booked
        # booking_instance = Booking.objects.get(pk=1)
        # price = booking_instance.get_price()
    
    