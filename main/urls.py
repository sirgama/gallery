from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='about'),
    path('search/', views.search_results, name='search_results'),
    path('image/<image_id>/', views.Imager.as_view(), name='imager'),
    re_path(r'details/(\d+)',views.detailed,name ='detailed'),
    path('location/<location>/', views.location_filter, name='location'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
