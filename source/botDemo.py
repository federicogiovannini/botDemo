import telegram

from telegram import Bot

# Start
TOKEN = "607283694:AAGk1aiS_11-c-cYHSwGVbfM34bb4TJ-x-4"

bot = telegram.Bot(token = TOKEN)

def start(bot, update):
	bot.send_message(chat_id = update.message.chat_id, text = "Ecco l'ultimo podcast disponibile")


from telegram.ext import Updater

updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher


from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

updater.start_polling()
