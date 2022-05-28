from django.shortcuts import render
from .models import Image, Location, Category
# Create your views here.

def home(request):
    images = Image.get_images()
    locations = Location.objects.all()
    return render(request, 'main/home.html', {'images':images, 'locations':locations})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_description(search_term)
        message = f"{search_term}"
        
        return render(request, 'main/search.html', {"message":message, "images":searched_images})
    else:
        message = "You havent searched for any terms"
        return render(request, 'main/search.html', {"message":message})