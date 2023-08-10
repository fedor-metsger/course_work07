
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    '''
    Выводит список всех публичных привычек
    '''
    queryset = Habit.objects.filter(public=True)
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitListMyAPIView(generics.ListAPIView):
    '''
    Выводит список всех привычек авторизованного пользователя
    '''
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user.id)


class HabitCreateAPIView(generics.CreateAPIView):
    '''
    Создаёт новую привычку
    '''
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    '''
    Выводит информацию о конкретной привычке.
    Доступна только для владельца привычки.
    '''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    '''
    Вносит изменения в привычку.
    Доступна только для владельца привычки.
    '''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    '''
    Удаляет указанную привычку из БД.
    Доступна только для владельца привычки.
    '''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
