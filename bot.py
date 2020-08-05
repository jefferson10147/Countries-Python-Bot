import logging
from configparser import ConfigParser
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from modules.emoji_flags import flags
from modules.request import get_country_by_name


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
config_parser = ConfigParser()
config_parser.read('config.ini')
TOKEN = config_parser['BOT']['token']
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = '*Rino says hi*')


def search(update, context):
    text = update.message.text

    if text in flags.keys():
        country_facts = get_country_by_name(flags[text])
    elif text in flags.values():
        country_facts = get_country_by_name(text)

    if country_facts == None:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "*Rino didn't find that country*")
    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text = country_facts)


def start_handlers_and_dispachers():
    start_handler = CommandHandler('start', start)
    search_handler = MessageHandler(Filters.text,search)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(search_handler)


if __name__ == '__main__':
    start_handlers_and_dispachers()
    updater.start_polling()
    updater.idle()