from django.contrib import admin
from .models import Booking


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'car_book', 'customer_firstname', 'customer_lastname',
        'customer_email', 'start_date', 'end_date', 'booking_date',
        'paid'
    ]
    list_filter = ['booking_date', 'car_book', 'paid']
