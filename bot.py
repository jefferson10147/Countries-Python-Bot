import logging
from configparser import ConfigParser
from telegram.ext import Updater
from telegram.ext import CommandHandler
from modules.emoji_flags import flags


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
config_parser = ConfigParser()
config_parser.read('config.ini')
TOKEN = config_parser['BOT']['token']
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = '*Rino says hi*')


def start_handlers_and_dispachers():
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)


if __name__ == '__main__':
    start_handlers_and_dispachers()
    updater.start_polling()
    updater.idle()