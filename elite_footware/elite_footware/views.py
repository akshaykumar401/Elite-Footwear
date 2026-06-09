from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'elite_footware/index.html', {'dummy_context': 'World'})