from django.shortcuts import render

# Create your views here.
def product_page(request):
  return render(request, 'product/product_page.html')