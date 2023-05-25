# Generated by Django 4.2.1 on 2023-05-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='esc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='image_url',
            field=models.URLField(default='https://'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(default='text', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.CharField(default='title', max_length=50),
            preserve_default=False,
        ),
    ]
