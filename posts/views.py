from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class HomePageView(ListView):
    # ListView automatically returns an object_list that you can loop over via the built-in for template tag.
    model = Post
    template_name='home.html'
    context_object_name="all_posts_list" # changes the name from object_list to all_posts_list 