from requests import get, post
from decouple import config
# from db_bot import DbBot


TOKEN = config('TOKEN')

URL_BASE = f"https://api.telegram.org/bot{TOKEN}"
URL_UPDATES = f"{URL_BASE}/getUpdates"
URL_SEND_MESSAGE = f"{URL_BASE}/sendMessage?"
URL_WEBHOOK = "https://amaurirg.ddns.net"
URL_SET_WEBHOOK = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={URL_WEBHOOK}"
URL_GET_WEBHOOK_INFO = f"{URL_WEBHOOK}/bot{TOKEN}/getWebhookInfo"


class BotFalar:
    def getme(self):
        self.resp_getme = get(f'{URL_BASE}/getMe').json()
        self.bot_name = self.resp_getme['result']['first_name']
        return self.bot_name

    def get_updates(self, offset = 0, timeout = 0):
        self.last_update_id = 0
        self.resp = get('{}?offset={}&timeout={}'.format(URL_UPDATES, offset, timeout)).json()
        self.result = len(self.resp['result'])
        if self.result >= 1:
            self.last_index = self.resp['result'][self.result - 1]
            self.chat = self.last_index['message']['chat']
            self.last_update_id = self.last_index['update_id']
            self.chat_id = self.chat['id']
            self.first_name = self.chat['first_name']
            self.text = self.last_index['message']['text']
            if 'username' in self.chat:
                self.username = self.chat['username']
            else:
                self.username = self.first_name
            self.handle_updates()
        return self.last_update_id

    def send_message(self, text):
        self.response = post(f"{URL_SEND_MESSAGE}chat_id={self.chat_id}&text={text}")
        return self.response.text

    def handle_updates(self):
        if self.text.startswith("/add"):
            self.add_item(self.text[5:])
            self.send_message(self.get_items())
        elif self.text.startswith("/del"):
            self.delete_item(self.text[5:])
            self.send_message(self.get_items())
        else:
            self.send_message(self.text[::-1])


# def set_webhook(self):
#     self.url_setwebhook = post(URL_SET_WEBHOOK)
#     return self.url_setwebhook
#
# def get_webhookinfo(self):
#     self.url_get_webhookinfo = get(URL_GET_WEBHOOK_INFO)
#     return self.url_get_webhookinfo


