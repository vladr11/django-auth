from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField(max_length=100, blank=False, default='')
