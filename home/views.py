from django.shortcuts import render
from .models import SlideImg

# Create your views here.
def index(request):
    slide = SlideImg.objects.all()
    return render(request, 'index.html', {'slide':slide})

def about(request):
    return render(request, 'about.html')