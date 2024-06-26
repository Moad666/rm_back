from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Rules(models.Model):
    ruleName = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    action = models.CharField(max_length=255)

class Categorie(models.Model):
    name = models.CharField(max_length=255)
    rule = models.ForeignKey(Rules, on_delete=models.CASCADE)



