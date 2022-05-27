from django.shortcuts import render
from .models import Image, Location, Category
# Create your views here.

def home(request):
    
    return render(request, 'main/home.html')
