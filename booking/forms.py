import re
from datetime import date
from django import forms
from .models import Booking


# add forms here
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'customer_firstname', 'customer_lastname', 'customer_email',
            'start_date', 'end_date',
        ]
        
        labels = {
            'customer_firstname': 'First Name',
            'customer_lastname': 'Last Name',
            'customer_email': 'Email',
            'start_date': 'Start Date',
            'end_date': 'Return Date',
            
        }
        
        widgets = {
            'customer_firstname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'customer_lastname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'customer_email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'start_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'min': date.today().strftime('%Y-%m-%d'),
                    'required': True
                }
            ),
            'end_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'min': date.today().strftime('%Y-%m-%d'),
                    'required': True
                }
            ),
        }
    