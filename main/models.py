
from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate


    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get( pk = id)
        return category
    
    
    def __str__(self):
        return self.title
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.title = update
        self.save()
    
    
    

class Category(models.Model):
    title = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
    
    
class Image(models.Model):
    main_image = models.ImageField(upload_to='gallery_media/')
    image_name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    @classmethod
    def update_image(cls,id, main_image,image_name, description, location, category):
        update = cls.objects.filter(id = id).update( image_name=image_name, description=description, location=location, category=category)
        return update
        
    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__title__icontains=search_term)
        return images
    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image
    
    @classmethod
    def filter_by_location(cls, img_location):
        images_location = cls.objects.filter(location__id=img_location)
        return images_location

    def __str__(self):
        return self.image_name