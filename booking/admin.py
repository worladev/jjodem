from django.contrib import admin
from .models import Booking


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'first_name', 'last_name', 'car_book', 'start_date', 'end_date', 'booking_date',
        'paid'
    ]
    list_filter = ['booking_date', 'car_book', 'paid']
    
    def first_name(self, obj):
        return obj.user.first_name
    
    def last_name(self, obj):
        return obj.user.last_name
    
    first_name.admin_order_field = 'user__first_name'
    last_name.admin_order_field = 'user__last_name'
    
