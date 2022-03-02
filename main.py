from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
from telegram import Update
import lang.responses as r
import os

# Begrüßung beim Hochfahren
def start_command(update: Update, context):
    update.message.reply_text('Ich blicke für dich in die Sterne...')

# Hier wird auf User geantwortet
def handle_message(update: Update, context):
    text = str(update.message.text).lower()
    response = r.sample_response(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} cause error {context.error}")


def main():
    load_dotenv()
    updater = Updater(token=os.getenv('TOKEN'), use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))

    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()

