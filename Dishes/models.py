from django.db import models

# Create your models here.
class Dishes(models.Model):
    name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    price = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.name
