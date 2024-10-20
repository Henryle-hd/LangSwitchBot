from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from typing import Final
import func
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN: Final = os.getenv("TOKEN")
BOT_USERNAME: Final = os.getenv("BOT_USERNAME")

# Store user language preferences
user_language_preferences = {}

# commands
async def start_co(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Please choose your language preference by typing:\n⚡ /english for English to Swahili\n⚡ /swahili for Swahili to English")

async def english(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_language_preferences[user_id] = "english"
    await update.message.reply_text("You have selected English to Swahili translation. Now enter the text you want to translate.")

async def swahili(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_language_preferences[user_id] = "swahili"
    await update.message.reply_text("You have selected Swahili to English translation. Now enter the text you want to translate.")

async def help_co(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("To use this bot:\n⚡ /english for English to Swahili translation\n⚡ /swahili for Swahili to English translation\nYou can always change your preference by using these commands.")

# handle messages based on user language preference
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    word = update.message.text

    # Check the user's language preference
    if user_id in user_language_preferences:
        if user_language_preferences[user_id] == "english":
            response = func.eng_to_ksw(word.lower())
        elif user_language_preferences[user_id] == "swahili":
            response = func.ksw_to_eng(word)
    else:
        # Default message if no language is chosen
        response = "Please choose a language using /english or /swahili."

    # Send the response
    try:
        await update.message.reply_text(response)
    except Exception as e:
        print(f"Error occurred: {e}")
        await update.message.reply_text("🔴\nThis service is unavailable now, please try again later.")

# error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Updates caused an error: {context.error}")

if __name__ == "__main__":
    print("starting...")

    # build
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler("start", start_co))
    app.add_handler(CommandHandler("english", english))
    app.add_handler(CommandHandler("swahili", swahili))
    app.add_handler(CommandHandler("help", help_co))

    # handle messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # error handler
    app.add_error_handler(error)

    # polling
    print("polling...")
    app.run_polling(poll_interval=3)
