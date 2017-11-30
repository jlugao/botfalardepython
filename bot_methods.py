from requests import get, post
from decouple import config
import json


TOKEN = config('TOKEN')

URL_BASE = "https://api.telegram.org/bot{}".format(TOKEN)
URL_UPDATES = "{}/getUpdates".format(URL_BASE)
URL_SEND_MESSAGE = "{}/sendMessage?".format(URL_BASE)
# URL_WEBHOOK = "https://"
# URL_SET_WEBHOOK = "https://api.telegram.org/bot{}/setWebhook?url={}".format(TOKEN, URL_WEBHOOK)
# URL_GET_WEBHOOK_INFO = "{}/bot{}/getWebhookInfo".format(URL_WEBHOOK, TOKEN)


class BotFalar:
    def getme(self):
        self.resp_getme = get('{}/getMe'.format(URL_BASE)).json()
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

    def send_message(self, text, reply_markup=None):
        self.message = "{}chat_id={}&text={}".format(URL_SEND_MESSAGE, self.chat_id, text)
        if reply_markup:
            self.message += "&reply_markup={}".format(reply_markup)
        return post(self.message)


    def handle_updates(self):
        # ***** elif self.text.startswith("/vote"): *****
        self.lives = self.get_lives()
        if self.text.startswith("/"):
            if self.text.startswith("/add"):
                self.add_item(self.text[5:])
                self.send_message(self.get_lives())
            elif self.text.startswith("/del"):
                self.delete_item(self.text[5:])
                # self.send_message(self.get_items())
            elif self.text.startswith("/list"):
                self.lives_list = ["{} - @{}\nVotos: {}\n".format(i[0], i[1], i[2]) for i in self.get_lives_list()]
                self.message = "\n".join(self.lives_list)
                self.send_message("Lives propostas\n\n{}".format(self.message))
            elif self.text.startswith("/vote"):
                self.keyboard = self.build_keyboard(self.lives)
                self.send_message("Escolha sua live ou\n/add <nome_da_live>\npara adicionar uma proposta de live",
                                  self.keyboard)
        else:
            # self.get_updates(self.last_update_id + 1)
            if self.text in self.lives:
                self.current_votes = self.len_votes(self.text)
                self.update_votes(self.text, self.current_votes[0] + 1)
                # self.send_message("Live {} recebeu mais um voto".format(self.text))
                self.send_message("@{} votou na Live '{}'".format(self.username, self.text))
            else:
                # self.send_message(self.text[::-1])
                # self.send_message("Olá {}, sou o {}, um bot de votação de lives para esse grupo.\n"
                #                   "Você pode:\n"
                #                   "Listar as Lives com /list\n"
                #                   "Votar na Live com /vote\n"
                #                   "Propor uma live com\n/add <nome_da_live>"
                #               .format(self.first_name, self.getme()))
                self.keyboard = self.build_keyboard(['/list', '/vote'])
                self.send_message("Olá {}, sou o {}, um bot de votação de lives para esse grupo.\n"
                                  "Escolha uma opção ou /add <nome_da_live> para propor uma live"
                                  .format(self.first_name, self.getme()), self.keyboard)


    def build_keyboard(self, items):
        keyboard = [[item] for item in items]
        reply_markup = {"keyboard": keyboard, "one_time_keyboard": True}
        return json.dumps(reply_markup)

# def set_webhook(self):
#     self.url_setwebhook = post(URL_SET_WEBHOOK)
#     return self.url_setwebhook
#
# def get_webhookinfo(self):
#     self.url_get_webhookinfo = get(URL_GET_WEBHOOK_INFO)
#     return self.url_get_webhookinfo


