import logging
from configparser import ConfigParser
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from modules.emoji_flags import flags
from modules.request import get_country_by_name
from modules.request import translate_text_into_flags
from modules.request import translate_flags_into_text


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

config_parser = ConfigParser()
config_parser.read("config.ini")
TOKEN = config_parser["BOT"]["token"]
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="*Rino says hi 🦏*"
    )


def search(update, context):
    text = update.message.text
    country_facts = None

    if text in flags.keys():
        country_facts = get_country_by_name(flags[text])

    elif ''.join([text[0].upper(), text[1:].lower()]) in flags.values():
        country_facts = get_country_by_name(text)

    else:
        country_facts = translate_text_into_flags(text)

    if country_facts:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=country_facts
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="*Rino didn't find that country🦏*"
        )


def translate(update, context):
    text = ' '.join(context.args)
    translated = translate_flags_into_text(text)
    
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=translated
    )


def start_handlers_and_dispachers():
    start_handler = CommandHandler("start", start)
    translate_flags_handler = CommandHandler("translate", translate)
    search_handler = MessageHandler(Filters.text, search)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(translate_flags_handler)
    dispatcher.add_handler(search_handler)


if __name__ == '__main__':
    start_handlers_and_dispachers()
    updater.start_polling()
    updater.idle()
