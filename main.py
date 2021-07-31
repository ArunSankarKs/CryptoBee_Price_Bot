import requests
import telebot
from variables import API_KEY, COINS_DICT

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["price"])
def price(message):
    if len(message["text"]) > 6:
        print(message)
        output = ""
        for contract in COINS_DICT.values():
            response = requests.get("https://api.pancakeswap.info/api/v2/tokens/{}".format(contract)).json()
            data = response["data"]
            output += data["symbol"] + " : $" + '%.10f' % float(data["price"]) + "\n"

        bot.reply_to(message, text="Hey, There! the current token status are as follows :\n \n" + output)


bot.polling()
