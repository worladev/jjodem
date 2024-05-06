from celery import shared_task
from django.core.mail import send_mail
from .models import Booking


@shared_task
def booking_created(booking_id):
    '''
    Task to send an e-mail notification when a booking
    is successfully created.
    '''
    booking = Booking.objects.get(id=booking_id)
    subject  = f'Booking nr. {booking.id}'
    message = f'Dear {booking.customer_firstname}, \n\n' \
            f'Your booking has been made successfully.' \
            f'Your booking ID is {booking.id}.'
    mail_sent = send_mail(
        subject,
        message,
        'support@jjodemlogistics.com',
        [booking.email]
        )
    return mail_sent
