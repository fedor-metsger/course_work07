
import datetime

from celery import shared_task

from habits.models import Habit
from habits.telegram import send_message


@shared_task
def check_habits():
    now_hour = datetime.datetime.now().hour
    now_minute = datetime.datetime.now().minute
    habits = Habit.objects.filter(time__hour=now_hour, time__minute=now_minute)
    # print("Selected habits ===============>")
    for h in habits:
        # print(h)
        action = h.action
        place = h.place
        time = h.time
        username = h.owner.telegram
        send_message(username, f'Вам нужно сделать {action} в {place} в {time}')
