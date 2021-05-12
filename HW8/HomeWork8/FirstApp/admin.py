from django.contrib import admin
from . import models

admin.site.register(
    [
        models.SlideShowPost,
        models.AboutPost,
        models.Services,
        models.ContactUs
    ]
)
# Register your models here.
