from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField(required=True)
  first_name = forms.CharField(max_length=100, required=True)
  last_name = forms.CharField(max_length=100, required=True)
  phone = forms.CharField(max_length=15, required=True)
  prefered_size = forms.FloatField(required=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'prefered_size']