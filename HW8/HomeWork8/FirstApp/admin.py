from django.contrib import admin
from . import models

admin.site.register(
    [
        models.SlideShowPost,
        models.AboutPost,
        models.Services
    ]
)
# Register your models here.
