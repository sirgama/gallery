from django.http import Http404
from django.shortcuts import render
from .models import Image, Location, Category
from django.views.generic.base import TemplateView
# Create your views here.

def home(request):
    images = Image.get_images()
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'main/home.html', {'images':images, 'categories': categories, "locations":locations})

def about(request):
    
    return render(request, 'main/about.html')


def search_results(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request, 'main/search.html', {"message":message, "images":searched_images, 'categories': categories, "locations":locations})
    else:
        message = "You havent searched for any terms"
        return render(request, 'main/search.html', {"message":message})
    

class Imager(TemplateView):
    template_name = 'main/gallery.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["imagelist"] = Image.objects.all()
        return context
    
def detailed(request, image_id):
    try:
        image = Image.objects.get(id = image_id)
    except:
        raise Http404()
    return render(request, 'main/detailed.html', {'image':image})


def location_filter(request, location):
    all_locations = Location.objects.all()
    a_location = Location.get_location_id(location)
    images = Image.filter_by_location(location)
    title = f'{a_location} Images'
    return render(request, 'main/location.html', {'title':title, 'images':images, 'locations':all_locations, 'location':a_location})