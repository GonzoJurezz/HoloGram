from telegram.ext import Updater
from lang.gen_horoscope import gen_horoskope
from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters


load_dotenv()

updater = Updater(token=os.getenv('TOKEN'), use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ich blicke in die Sterne")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=gen_horoskope())


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()
