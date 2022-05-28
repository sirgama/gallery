from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('search/', views.search_results, name='search_results'),
   
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
