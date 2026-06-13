from django.shortcuts import render

# Create your views here.
def about_page(request):
  return render(request, 'about_us/about_page.html')