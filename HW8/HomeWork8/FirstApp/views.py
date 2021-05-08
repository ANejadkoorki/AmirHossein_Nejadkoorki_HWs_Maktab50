from django.shortcuts import render
from . import models

# Create your views here.

def home_view(request):
    """
    it`s a view for home part of page!!!
    """
    slide_show_posts = models.SlideShowPost.objects.all()
    return render(request,
                  context={
                    "slide_show_posts" : slide_show_posts
                  },
                  template_name="FirstApp/home.html"
                  )
