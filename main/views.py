from django.shortcuts import render
from .models import Image, Location, Category
from django.views.generic.base import TemplateView
# Create your views here.

def home(request):
    images = Image.get_images()
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'main/home.html', {'images':images, 'categories': categories, "locations":locations})

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