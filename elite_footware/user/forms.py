# pyrefly: ignore [missing-import]
from django import forms
# pyrefly: ignore [missing-import]
from django.contrib.auth.forms import UserCreationForm
# pyrefly: ignore [missing-import]
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField(required=True)
  first_name = forms.CharField(max_length=100, required=True)
  last_name = forms.CharField(max_length=100, required=True)
  phone = forms.IntegerField(required=True)
  prefered_size = forms.FloatField(required=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'prefered_size']