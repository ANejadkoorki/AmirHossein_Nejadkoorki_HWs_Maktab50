# Generated by Django 3.2.1 on 2021-05-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0002_slideshowpost_uploads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshowpost',
            name='caption',
            field=models.CharField(max_length=800, verbose_name='caption'),
        ),
    ]