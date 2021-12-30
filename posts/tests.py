from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.
# Test functions should have the name test_ will be run as tests.
# The remaining functions are helper functions.

# Testing the model
class PostModelTest(TestCase):
    def setUp(self):
        # Create a sample test database
        Post.objects.create(text='just a test')
        # We create a single entry in this database
    
    def test_text_content(self):
        post=Post.objects.get(id=1)
        # Django starts indexing at 1
        expected_object_name=f'{post.text}'
        self.assertEqual(expected_object_name,'just a test')
        
# Testing the homepage
class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')
    
    def test_view_url_exists_at_proper_location(self):
        resp=self.client.get('/')
        self.assertEqual(resp.status_code,200)
        # Test whether the home page actually exists
    
    def test_view_url_by_name(self):
        resp=self.client.get(reverse('home')) # Using the url rather than name
        self.assertEqual(resp.status_code,200)
    
    def test_view_uses_correct_template(self):\
        # Test whether the view is using the right template
        resp=self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'home.html')
        
    
    