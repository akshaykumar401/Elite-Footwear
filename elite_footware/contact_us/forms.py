from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ['full_name', 'email', 'subject', 'message']

    widgets = {
      'full_name': forms.TextInput(attrs={'placeholder': ' '}),
      'email': forms.EmailInput(attrs={'placeholder': ' '}),
      'subject': forms.TextInput(attrs={'placeholder': ' '}),
      'message': forms.Textarea(attrs={'placeholder': ' ', 'rows': 5}),
    }
  