from django.db import models
from django.db.models import Model

class People(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    phone_no = models.IntegerField()

    def __str__(self):
        return self.name