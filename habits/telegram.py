
import os
import requests

from django.db.models import Max
from users.models import User


def get_updates(last_update):
    tg_token = os.getenv("TG_BOT_TOKEN")
    return requests.get(f'https://api.telegram.org/bot{tg_token}/getUpdates?offset={last_update + 1}').json()


def parse_updates(updates: dict):
    for u in updates:
        user = User.objects.get(telegram=u["message"]["chat"]["username"])
        if User.objects.filter(telegram=user).exists():
            user.chat_id = u["message"]["chat"]["id"]
            user.update_id = u["update_id"]
            user.save()


def send_message(username, text):
    last_update = User.objects.aggregate(Max('update_id'))['update_id__max']
    updates = get_updates(last_update)
    if updates["ok"]:
        parse_updates(updates["result"])

    chat_id = User.objects.get(telegram=username).chat_id
    if not chat_id:
        print("Can not get user chat ID.")
        return

    data_for_request = {"chat_id": chat_id, "text": text}
    response = requests.get(f'https://api.telegram.org/bot{os.getenv("TG_BOT_TOKEN")}/sendMessage', data_for_request)
    return response.json()
