# Generated by Django 4.0.4 on 2022-05-27 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='main_image',
            field=models.ImageField(upload_to='gallery_media/'),
        ),
    ]
