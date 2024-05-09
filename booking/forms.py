import re
from datetime import date
from django import forms
from .models import Booking


# add forms here
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'start_date', 'end_date',
        ]
        
        labels = {
            'start_date': 'Start Date',
            'end_date': 'Return Date',
            
        }
        
        widgets = {
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
    