from django.db import models


# Create your models here.

class model_tests(models.Model):
    user_id = models.IntegerField()
    fav_sub = models.CharField(max_length=100)
