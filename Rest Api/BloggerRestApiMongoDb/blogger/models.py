from django.db import models

# Create your models here.
class Blogger(models.Model):
    userId = models.CharField(max_length=70,blank=False)
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField(max_length=500,blank=False, default='')