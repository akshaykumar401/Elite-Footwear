from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def contact_page(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request, 'contact_us/contact_page.html', {
        'form': ContactForm(),
        'success': True
      })
  else:
    form = ContactForm()
  return render(request, 'contact_us/contact_page.html', {
    'form': form
  })