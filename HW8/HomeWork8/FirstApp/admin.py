from django.contrib import admin
from . import models

admin.site.register(
    [
        models.SlideShowPost
    ]
)
# Register your models here.
