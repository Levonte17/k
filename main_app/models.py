from django.db import models
from django.urls import reverse

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField
    time = models.CharField
    location = models.CharField

def __str__(self):
    return self.name
def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id })
