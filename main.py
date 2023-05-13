import os
import telebot

# Retrieve the token from the environment variable
token = os.getenv('token')

# Create a new instance of the TeleBot class with the retrieved token
bot = telebot.TeleBot(token)

# Handler for the '/start' command
@bot.message_handler(commands=['start'])
def start_command(message):
    response_text = "Hello! Welcome to this bot!\n\n"
    response_text += "For help, use the command /help."
    bot.reply_to(message, response_text)

# Handler for the '/help' command
@bot.message_handler(commands=['help'])
def help_command(message):
    response_text = "Here are the available commands:\n\n"
    response_text += "/start - Start the bot.\n"
    response_text += "/help - Show this help message.\n"
    bot.reply_to(message, response_text)

# Handler for any other message
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, message.text)

# Start the bot and keep it running
bot.infinity_polling()

# The code execution reaches this point only if the bot is stopped or encounters an error
# The bot will continuously listen for new messages and respond accordingly
# You can terminate the program to stop the bot
