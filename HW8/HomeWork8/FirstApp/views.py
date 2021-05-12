from django.shortcuts import render

from . import models


# Create your views here.

def home_view(request):
    """
    it`s a view for home part of page!!!
    """
    slide_show_posts = models.SlideShowPost.objects.all()
    about_post = models.AboutPost.objects.all()
    services = models.Services.objects.all()
    return render(request,
                  context={
                      "slide_show_posts": slide_show_posts,
                      "about_post": about_post,
                      "services_post": services,
                  },
                  template_name="FirstApp/home.html"
                  )
