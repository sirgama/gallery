from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestCLass(TestCase):
    #Set up Method
    def setUp(self):
        self.loc = Location(name="Kenya")
        self.loc.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.loc,Location))

    def test_save_method(self):
        self.loc.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.loc.save_location()
        self.loc.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update(self):
        location = Location.get_location_id(self.loc.id)
        location.update_location('Microsoft')
        location = Location.get_location_id(self.loc.id)
        self.assertTrue(location.name == 'Microsoft')


class CategoryTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Category(title="Fashion")
        self.cat.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))

    def test_save_method(self):
        self.cat.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.cat.save_category()
        self.cat.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update(self):
        category = Category.get_category_id(self.cat.id)
        category.update_category('children')
        category = Category.get_category_id(self.cat.id)
        self.assertTrue(category.title == 'children')




class ImageTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Category(name="fashion")
        self.cat.save_category()

        self.loc = Location(name="Lucan")
        self.loc.save_location()

        self.image = Image(image_name='image test', description='my test',location=self.loc, category=self.cat)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()
        self.cat.delete_category()
        self.loc.delete_location()


    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)


    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images) == 1)

    def test_search_by_category(self):
        images = Image.search_by_category('fashion')
        self.assertTrue(len(images)>0)

    def test_filter_by_location(self):
        images = Image.filter_by_location('1')
        print(images)
        self.assertTrue(len(images)>0)

    def test_update_image(self):
        self.image.save_image()
        image = Image.update_image( self.image.id, 'test update', 'my test',self.loc, self.cat)
        upimage = Image.objects.filter(id = self.image.id)
        print(upimage)
        self.assertTrue(Image.name == 'test update')