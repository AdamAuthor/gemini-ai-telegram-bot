import os
import telebot
from domain_layer import get_response

TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
bot = telebot.TeleBot(TELEGRAM_API_KEY)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    help_text = """Welcome to the Gemini AI Bot! 🤖
    
This bot is integrated with Gemini AI. You can ask it questions and it will provide answers based on its AI capabilities.

Here's how to use it:

1. Simply type your question in the chat and send it.
2. The bot will process your question and provide an answer as soon as possible.

Please note that the quality of the answer depends on the complexity of the question. The bot is designed to handle a wide range of topics, but it might not be able to answer very specific or complex questions.

Enjoy using the Gemini AI Bot!
    """
    bot.reply_to(message, help_text)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    wait_message = bot.reply_to(message, "Please wait... 🕐")
    response = get_response(message.text)
    bot.delete_message(wait_message.chat.id, wait_message.message_id)
    bot.reply_to(message, response.text)


bot.infinity_polling()
