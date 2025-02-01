from django.db import models

class Django_Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()


