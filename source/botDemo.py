import telegram

AUDIO_URL = "http://audio.radio24.ilsole24ore.com/radio24_audio/2018/180518-lazanzara-s.mp3"

# Start
TOKEN = "607283694:AAGk1aiS_11-c-cYHSwGVbfM34bb4TJ-x-4"


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def start(bot, update):
	AUDIO_URL = "http://audio.radio24.ilsole24ore.com/radio24_audio/2018/180518-lazanzara-s.mp3"
	episodes_list = [ AUDIO_URL, ]
	button_list = [ [InlineKeyboardButton( text=(s.split("/")[-1] or '').split("-")[0] or s, url=s )] for s in episodes_list ]

	reply_markup = InlineKeyboardMarkup( util.build_menu( button_list, n_cols=1) )

	bot.send_message( chat_id=update.message.chat_id, text="Ecco gli ultimi podcast disponibili", reply_markup=reply_markup )



from telegram.ext import Updater

updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher


from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

updater.start_polling()
