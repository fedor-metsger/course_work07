
import os
import requests

from django.db.models import Max
from users.models import User


def get_updates(last_update):
    tg_token = os.getenv("TG_BOT_TOKEN")
    response = requests.get(f'https://api.telegram.org/bot{tg_token}/getUpdates?offset={last_update + 1}')
    res = response.json()
    return res

def parse_updates(updates: dict):
    for u in updates:
        username = u["message"]["chat"]["username"]
        chat_id = u["message"]["chat"]["id"]
        update_id = u["update_id"]
        # print("chat_id:", chat_id, "username:", username, "update_id:", update_id)
        if User.objects.filter(telegram=username).exists():
            user = User.objects.get(telegram=username)
            user.chat_id = chat_id
            user.update_id = update_id
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

    print(f'Chat ID: {chat_id}.')
    data_for_request = {
        "chat_id": chat_id,
        "text": text
    }
    tg_token = os.getenv("TG_BOT_TOKEN")
    response = requests.get(f'https://api.telegram.org/bot{tg_token}/sendMessage', data_for_request)
    return response.json()