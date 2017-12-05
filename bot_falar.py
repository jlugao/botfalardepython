from db_bot import DbBot
from bot_methods import BotFalar
from decouple import config

TOKEN = config('TOKEN')

db = DbBot()
db.setup()

bot = BotFalar(db,TOKEN)
bot.get_updates()






def main():
    

    
    last_id = 0
    while True:
        last_id = bot.get_updates(last_id + 1, 30)
        # print("Aguardando mensagens...")
        # print(last_id)


#if __name__ == '__main__':
#    main()
