# Generated by Django 3.2.1 on 2021-05-12 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0003_alter_slideshowpost_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshowpost',
            name='uploads',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='image'),
        ),
    ]
