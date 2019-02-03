from django.db import models


class Product(models.Model):
    """
    Dummy model class to test auth functionality.
    """
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200, blank=False, default='')
