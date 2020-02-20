from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    street = models.CharField('Street', max_length=255)
    postcode = models.CharField('Street', max_length=255)
