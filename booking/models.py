from django.db import models
from rentals.models import CarModel
from django.utils import timezone


# Create your models here.
class Booking(models.Model):
    # user = models.ForeignKey('User', on_delete=models.CASCADE)
    car_book = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    customer_firstname = models.CharField(max_length=25)
    customer_lastname = models.CharField(max_length=25)
    customer_email = models.EmailField(max_length=50)
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
    
    