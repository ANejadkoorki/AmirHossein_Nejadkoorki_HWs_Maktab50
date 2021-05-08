from django.db import models


# Create your models here.


class SlideShowPost(models.Model):
    title = models.CharField(verbose_name='title of post', max_length=200)
    caption = models.TextField(verbose_name='caption')
