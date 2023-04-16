from django.db import models

# Create your models here.
class DatabrickModel(models.Model):
    instruction = models.TextField()
    context=models.TextField(blank=True)
    response=models.TextField()
    category=models.CharField(max_length=250)