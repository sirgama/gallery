from django.shortcuts import render
from .models import Image, Location, Category
# Create your views here.

def home(request):
    images = Image.get_images()
    locations = Location.objects.all()
    return render(request, 'main/home.html', {'images':images, 'locations':locations})
