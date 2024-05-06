from django.shortcuts import render, redirect, reverse, get_object_or_404
from decimal import Decimal
from django.conf import settings
from booking.models import Booking


# Create your views here.
# create the hubtel instance

def process_payment(request):
    # booking_id = request.session.get('booking_id', None)
    # booking = get_object_or_404(Booking, id=booking_id)
    
    # if request.method == 'POST':
        # form = PaymentMethodForm(request)
        # if form.is_valid():
            
        # success_url = request.build_absolute_uri(
        #     reverse('payment:completed')
        # )
        # cancel_url = request.build_absolute_uri(
        #     reverse('payment:canceled')
        # )
        
        # hubtel checkout session data
        
        # checkbox
    return render(request, 'payment/process-payment.html')
    

def payment_completed(request):
    return render(request, 'payment/completed.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
        
