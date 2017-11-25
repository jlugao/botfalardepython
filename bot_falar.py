from db_bot import DbBot




bot = DbBot()
bot.setup()

def main():
    last_id = 0
    while True:
        print("Aguardando mensagens...")
        last_id = bot.get_updates(last_id + 1, 5)
        print(last_id)


if __name__ == '__main__':
    main()
