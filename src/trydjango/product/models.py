from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    price       = models.DecimalField(max_digits=100, decimal_places=2)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField()