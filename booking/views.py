from django.urls import reverse
from django.shortcuts import render, redirect
# from .models import Booking
from rentals.models import CarModel
from .forms import BookingForm
# from django.contrib import messages
from .tasks import booking_created
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def book_car(request, car_id):
    car_to_book = CarModel.objects.get(pk=car_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            
            # populate user details required fields
            booking.user = request.user
            booking.car_book = car_to_book
                
            booking_created.delay(car_id) # add asynchronous task
            request.session['car_id'] = car_id
            booking.paid = False
            booking.save()
            return redirect(reverse('payment:process'))
    else:
        initial_data = {
            'car_book_id': car_id,
            'first_name':request.user.first_name,
            'last_name':request.user.last_name
            }
       
        form = BookingForm(initial=initial_data)
        
    context = {
        'form': BookingForm,
        'car_to_book': car_to_book
    }
    return render(request, 'booking/book-car.html', context)
