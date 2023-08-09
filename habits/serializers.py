
from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitLengthValidator, NiceHabitValidator, \
    LinkedAndRewardValidator, LinkedIsNiceValidator, HabitPeriodValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitLengthValidator(), NiceHabitValidator(),
                      LinkedAndRewardValidator(), LinkedIsNiceValidator(),
                      HabitPeriodValidator()]
