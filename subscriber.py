import logging
import telegram
import os
# import platform
import psycopg2
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# print(platform.python_version())
bot_token = os.getenv("BOT_TOKEN")


def store_in_database(telegram_id, phone_number):

    # establish connection to database
    connection = psycopg2.connect(
        dbname="postgres",
        # dbname="rsnpostdb",
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port="port"
    )

    # create cursor object
    cursor = connection.cursor()

    try:
        # prepare INSERT INTO statement with clause for updating phone number if repeated
        insert_query = """INSERT INTO subscriber_list (telegram_id, phone_number) 
                            VALUES (%s,%s)
                            ON CONFLICT (telegram_id)
                            DO UPDATE SET phone_number=excluded.phone_number"""

        # execute SQL command
        cursor.execute(insert_query,
                       (telegram_id, phone_number)
                       )
        # commit changes to database
        connection.commit()
    except psycopg2.Error as e:
        logging.error(f"Database error: {e}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [KeyboardButton(text="Send your phone number", request_contact=True)]
    ]

    try:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! To complete your subscription or update your phone number, please press the button below.", reply_markup=ReplyKeyboardMarkup(keyboard), parse_mode='HTML')
    except Exception as e:
        logging.error(f"{e}")


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone_number = update.effective_message.contact.phone_number
    telegram_id = update.effective_chat.id

    try:
        store_in_database(telegram_id, phone_number)

        await update.message.reply_text(
            "You are now subscribed.",
            reply_markup=ReplyKeyboardRemove()
        )

    except Exception as e:
        logging.error(f"{e}")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="There was a problem with your subscription.")

    logging.info(
        f"Subscription info - Telegram ID: {telegram_id}, Phone Number: {phone_number}")


async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Got feedback? We'd love to hear it! Click the link below to share your thoughts with us.\n\n👉 [Form Link] https://not_a_valid_link.sg \n\nP.S. Your feedback is anonymous, but feel free to include your name if you'd like a follow-up.😀"

    try:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode='HTML', protect_content=True)
    except Exception as e:
        logging.error(f"{e}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(bot_token).build()

    start_handler = CommandHandler('start', start)
    feedback_handler = CommandHandler('feedback', feedback)
    contact_handler = MessageHandler(filters.CONTACT, contact)

    application.add_handler(start_handler)
    application.add_handler(contact_handler)
    application.add_handler(feedback_handler)

    application.run_polling()
