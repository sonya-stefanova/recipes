# Generated by Django 4.2.1 on 2023-05-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_recipe_description_recipe_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]