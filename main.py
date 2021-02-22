import logging

from bs4 import BeautifulSoup
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Function for start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Salam 👑\nFake Mail almaq üçün bir botdur 🎉\n/generate yazaraq Fake Mail əldə edə bilərsiz.\n\nSahibim: @c9ala\nBotlar: @c9alabots\n\n-----------------------\n\nHi 👑 Fake Mail is a bot to get 🎉\nYou can get Fake Mail by typing /generate .\n\nOwner: @c9ala\nOther Bots: @c9alabots')

# Function for generate fake mail
def generate_command(update: Update, context: CallbackContext) -> None:
    req = requests.get("https://generator.email/")
    res = BeautifulSoup(req.content, "html.parser")
    soup = res.find_all('input')
    email = f"{soup[0].get('value')}@{soup[1].get('value')}"
    update.message.reply_text(f'Email Yaradıldı📌✨ / Email Generate📌✨: {email}')

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1622168622:AAEmnhDwV_NVKYrDXbEF-BwFE4t6SnirqX4", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("generate", generate_command))

    # on noncommand i.e message - echo the message on Telegram
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
