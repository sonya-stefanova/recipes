from django.db import models

# Create your models here.
class Recipe(models.Model):
    TITLE_MAX_LEN = 30
    INGREDIENT_MAX_LEN = 250

    title = models.CharField(
    max_length=TITLE_MAX_LEN,
    )


    image_url = models.URLField()

    description = models.TextField()

    ingredients = models.CharField(
        max_length=INGREDIENT_MAX_LEN,
    )

    time = models.IntegerField()


    def __str__(self):
        return self.title
