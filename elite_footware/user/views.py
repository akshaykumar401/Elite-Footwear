from django.shortcuts import render

# Create your views here.
def user_page(request):
  return render(request, 'user/user_page.html')