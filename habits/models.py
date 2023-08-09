
from django.db import models

from config import settings


# Create your models here.
class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    place = models.CharField(max_length=150, verbose_name='место', null=True, blank=True)
    time = models.TimeField(verbose_name='время', null=True, blank=True)
    action = models.CharField(max_length=150, verbose_name='действие')
    nice = models.BooleanField(default=False, verbose_name='приятная')
    linked = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    period = models.SmallIntegerField(verbose_name='периодичность', null=True, blank=True)
    reward = models.CharField(max_length=150, verbose_name='вознаграждение', null=True, blank=True)
    length = models.SmallIntegerField(verbose_name='продолжительность')
    public = models.BooleanField(default=False, verbose_name='публичная')

    def __str__(self):
        return f'Habit({self.action})'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
