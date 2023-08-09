
from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView, HabitListMyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/my/', HabitListMyAPIView.as_view(), name='habit_my'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habit/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habit_destroy'),
]
