from db_bot import DbBot


bot = DbBot()
bot.setup()


def main():
    last_id = 0
    while True:
        last_id = bot.get_updates(last_id + 1, 5)
        # print("Aguardando mensagens...")
        # print(last_id)


if __name__ == '__main__':
    main()
