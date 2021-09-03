from django.db import models

class database_add_test(models.Model):
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=100)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
