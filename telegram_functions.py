import logging
import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
# Lädt die Umgebungsvariablen aus der .env-Datei
load_dotenv()
debug = os.environ.get("DEBUG", False)
logger = logging.getLogger(__name__)
# Funktionen für den Telegram-Chatbot
def start(update, context):
    update.message.reply_text("Hi, ich bin der Micro-ChatBot von DeepCore Developers integriert mit ChatGPT. Schreib mir eine Nachricht, und ich werde versuchen, dir zu antworten.")
def chat(update, context):
    text = update.message.text
    response = generate_response(text)
    update.message.reply_text(response)
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
def main():
    # Telegram-Bot starten und Nachrichten verarbeiten
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        logger.error("TELEGRAM_TOKEN environment variable is not set")
        return
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)
    chat_handler = MessageHandler(Filters.text, chat)
    dispatcher.add_handler(chat_handler)
    # Error-Handler hinzufügen 3e
    dispatcher.add_error_handler(error)
    try:
        # Den Bot starten
        updater.start_polling()
        updater.idle()
    except Exception as e:
        logger.exception("An error occurred: %s", e)
if __name__ == "__main__":
    main()