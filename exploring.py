# -*- coding: utf-8 -*-
from decouple import config
import requests
import json

token = config('TOKEN')

BASE_URL = f'https://api.telegram.org/bot{token}/'


def get_me():
    bot = requests.get(f'{BASE_URL}getme').json()
    return bot

def get_update(update_id):
    bot = requests.get(f'{BASE_URL}getupdates?offset={update_id}')
    return json.loads(bot.content)
    #return bot.json()

def send_message(chat_id, text):
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(f'{BASE_URL}sendmessage', data)
    return response

def username():
    bot = requests.get(f'{BASE_URL}getupdates').json()
    return bot['result'][-1]['message']['from']['username']
    