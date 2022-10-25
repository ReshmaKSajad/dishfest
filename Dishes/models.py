from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dishes(models.Model):
    name = models.CharField(max_length = 200)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    category = models.CharField(max_length = 200)
    price = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.name
