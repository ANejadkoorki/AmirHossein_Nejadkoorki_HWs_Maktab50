from django.shortcuts import render

from . import models, forms


# Create your views here.

def home_view(request):
    """
    it`s a view for home part of page!!!
    """
    slide_show_posts = models.SlideShowPost.objects.all()
    about_post = models.AboutPost.objects.all()
    services = models.Services.objects.all()
    form_instance = forms.PostForm()
    if request.method == 'POST':
        form_instance = forms.PostForm(data=request.POST)
        if form_instance.is_valid():
            form_instance.save()
    return render(request,
                  context={
                      "slide_show_posts": slide_show_posts,
                      "about_post": about_post,
                      "services_post": services,
                      "post_form": form_instance
                  },
                  template_name="FirstApp/home.html"
                  )
