from django.db import models

# Create your models here.


class Clients(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    bottles_ordered = models.IntegerField(default=0)



