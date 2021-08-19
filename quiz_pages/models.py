from django.db import models

# Create your models here.

class model_test(models.Model):
    fav_sub = models.CharField(max_length=100)
