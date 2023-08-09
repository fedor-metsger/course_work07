
from rest_framework import serializers

from habits.models import Habit


class HabitLengthValidator():
    def __call__(self, value):
        length = dict(value).get("length")
        if length > 120:
            raise serializers.ValidationError("Длительность привычки не может быть больше 120 секунд")


class HabitPeriodValidator():
    def __call__(self, value):
        period = dict(value).get("period")
        if period > 7:
            raise serializers.ValidationError("Привычка должна выполняться не реже, чем раз в 7 дней")


class LinkedAndRewardValidator():
    def __call__(self, value):
        linked = dict(value).get("linked")
        reward = bool(str(dict(value).get("reward")))
        if linked and reward:
            raise serializers.ValidationError(
                "У привычки не может быть одновременно вознаграждения и связанной привычки")


class NiceHabitValidator():
    def __call__(self, value):
        nice = dict(value).get("nice")
        linked = dict(value).get("linked")
        reward = bool(str(dict(value).get("reward")))
        if nice and linked or nice and reward:
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки")


class LinkedIsNiceValidator():
    def __call__(self, value):
        linked = dict(value).get("linked")
        if linked:
            hab = Habit.objects.get(pk=linked.id)
            if not hab.nice:
                raise serializers.ValidationError("Связанная привычка должна быть приятной")
