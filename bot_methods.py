from requests import get, post

import json

# URL_WEBHOOK = "https://"
# URL_SET_WEBHOOK = "https://api.telegram.org/bot{}/setWebhook?url={}".format(TOKEN, URL_WEBHOOK)
# URL_GET_WEBHOOK_INFO = "{}/bot{}/getWebhookInfo".format(URL_WEBHOOK, TOKEN)


class BotFalar:
    def __init__(self,database,TOKEN):
        self.db = database
        self.URL_BASE = "https://api.telegram.org/bot{}".format(TOKEN)
        self.URL_UPDATES = "{}/getUpdates".format(self.URL_BASE)
        self.URL_SEND_MESSAGE = "{}/sendMessage?".format(self.URL_BASE)
    
    def get_me(self):
        self.resp_getme = get('{}/getMe'.format(self.URL_BASE)).json()
        self.bot_name = self.resp_getme['result']['first_name']
        return self.bot_name

    def get_updates(self, offset = 0, timeout = 0):
        dict_updates = {'last_update_id': 0}
        resp = get('{}?offset={}&timeout={}'.format(self.URL_UPDATES, offset, timeout)).json()
        result = len(resp['result'])
        if result >= 1:
            dict_updates['last_index'] = resp['result'][result - 1]
            dict_updates['chat'] = dict_updates['last_index']['message']['chat']
            dict_updates['last_update_id'] = dict_updates['last_index']['update_id']
            dict_updates['chat_id'] = dict_updates['chat']['id']
            dict_updates['first_name'] = dict_updates['chat']['first_name']
            dict_updates['text'] = dict_updates['last_index']['message']['text']
            if 'username' in dict_updates['chat']:
                dict_updates['username'] = dict_updates['chat']['username']
            else:
                dict_updates['username'] = dict_updates['first_name']
        return dict_updates

    def send_message(self, text, chat_id, reply_markup=None):
        self.message = "{}chat_id={}&text={}".format(self.URL_SEND_MESSAGE, chat_id, text)
        if reply_markup:
            self.message += "&reply_markup={}".format(reply_markup)
        return post(self.message)


    def handle_updates(self, offset = 0, timeout = 0):
        
        dict_updates = self.get_updates(offset, timeout)
        
        lives = self.db.get_lives()
        if dict_updates['text'].startswith("/"):
            
            if dict_updates['text'].startswith("/add"):
                self.db.add_item(dict_updates['text'][5:], dict_updates['username'])
                self.send_message(self.db.get_lives(), dict_updates['chat_id'])
                
            elif dict_updates['text'].startswith("/del"):
                self.db.delete_item(dict_updates['text'][5:])
                
            elif dict_updates['text'].startswith("/list"):
                self.db.lives_list = ["{} - @{}\nVotos: {}\n".format(i[0], i[1], i[2]) for i in self.db.get_lives_list()]
                message = "\n".join(self.lives_list)
                self.send_message("Lives propostas\n\n{}".format(message), dict_updates['chat_id'])
                
            elif dict_updates['text'].startswith("/vote"):
                keyboard = self.build_keyboard(lives)
                self.send_message("Escolha sua live ou\n/add <nome_da_live>\npara adicionar uma proposta de live",
                                  dict_updates['chat_id'],
                                  keyboard)
        else:

            if dict_updates['text'] in lives:
                self.current_votes = self.len_votes(dict_updates['text'])
                self.update_votes(dict_updates['text'], self.current_votes[0] + 1)
                self.send_message("@{} votou na Live '{}'".format(dict_updates['username'], dict_updates['chat_id'],
                                  dict_updates['text']))
            else:
                keyboard = self.build_keyboard(['/list', '/vote'])
                self.send_message("Olá {}, sou o {}, um bot de votação de lives para esse grupo.\n"
                                  "Escolha uma opção ou /add <nome_da_live> para propor uma live"
                                  .format(dict_updates['first_name'], self.get_me()), dict_updates['chat_id'], keyboard)
        
        return dict_updates['last_update_id']


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


