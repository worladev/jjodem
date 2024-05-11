from django import forms
# from django.contrib.auth.models import User
from account.models import CustomUser



# Create your forms here
class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    

# User Registration
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'address', 'phone_number']
    
    def clean_password2(self):
        clean_data = self.cleaned_data
        if clean_data['password'] != clean_data['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return clean_data['password2']
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if CustomUser.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data


# 
class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'address', 'phone_number']
        
    def clean_email(self):
        data = self.cleaned_data['email']
        query = CustomUser.objects.exclude(id=self.instance.id).filter(email=data)
        if query.exists():
            raise forms.ValidationError('Email already in use.')
        return data
    
    