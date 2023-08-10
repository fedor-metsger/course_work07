
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    telegram = models.CharField(max_length=50, unique=True, verbose_name='никнейм в телеграм')
    chat_id = models.PositiveBigIntegerField(default=0, null=True, blank=True, verbose_name='номер чата')
    update_id = models.PositiveBigIntegerField(
        default=0, null=True, blank=True, verbose_name='номер последнего сообщения')

    USERNAME_FIELD = "telegram"
    REQUIRED_FIELDS = []
