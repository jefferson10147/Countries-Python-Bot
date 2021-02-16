# Telegram Bot
This is a Telegram bot using python 3.

## What does this bot? 
This bot can gives a simple country information, just receiving an emoji flag like '🏴󠁧󠁢󠁷󠁬󠁳󠁿' or country name (in english) like 'Wales'. Here's the [API](https://restcountries.eu) this bot uses to consult countries data. Also this bot can encrypt messages using flags emojis, just send any message and bot will send you the encrypted message.
## How to run this bot on your linux machine
* You need to install telegram bot library:
```bash
$ pip install python-telegram-bot
```

* Make a config.ini file where you have to put telegram API data:
```
[BOT]
token = YOUR_BOT_TELEGRAM_API_TOKEN
```

* Then just run on your terminal:
```bash
$ python3 bot.py
 ```

### Special Thanks

* Marco Useche, who gave me the idea for this bot.
* Pedro Labrador, who created emojis dictionary. 
