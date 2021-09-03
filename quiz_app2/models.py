from django.db import models


# Create your models here.

class model_tests(models.Model):
    user_id = models.IntegerField()
    fav_sub = models.CharField(max_length=100)

class database_test(models.Model):
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=100)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)