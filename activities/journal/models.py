from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=100)
    subject = models.TextField()

class Activity(models.Model):
    name = models.CharField(max_length=50)
    frequency = models.PositiveIntegerField()
    type = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)


