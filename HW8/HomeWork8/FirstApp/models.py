from django.db import models


# Create your models here.


class SlideShowPost(models.Model):
    title = models.CharField(verbose_name='title of post', max_length=200)
    caption = models.CharField(verbose_name='caption', max_length=800)
    uploads = models.ImageField(verbose_name='image', blank=True, null=True)


class AboutPost(models.Model):
    text = models.TextField(verbose_name='text')


class Services(models.Model):
    created_date = models.DateTimeField(verbose_name="Date of Create", auto_now_add=True)
    title = models.CharField(verbose_name="Title", max_length=100)
    content = models.TextField(verbose_name="Body")
