from django.db import models

# Create your models here.

class JOb(models.Model):
    Image=models.ImageField(upload_to='Images/')
    Summary =models.CharField(max_length=200)