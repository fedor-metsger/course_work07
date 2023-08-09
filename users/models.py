
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    telegram = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = "telegram"
    REQUIRED_FIELDS = []
