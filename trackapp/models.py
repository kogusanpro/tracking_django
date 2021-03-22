from django.db import models

class Tracks(models.Model):
   url = models.CharField(max_length=100)
   keywords = models.CharField(max_length=100)
   created_time = models.DateTimeField(auto_now_add=True)
   updated_time = models.DateTimeField(auto_now=True)