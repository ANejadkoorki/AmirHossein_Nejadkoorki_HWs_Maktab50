from django.shortcuts import render


# Create your views here.

def home_view(request):
    """
    it`s a view for home part of page!!!
    """
    return render(request,
                  template_name="blog/home.html"
                  )
