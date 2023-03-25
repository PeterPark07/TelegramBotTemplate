import telebot

bot = telebot.TeleBot("YOUR TOKEN HERE")

@bot.message_handler(commands=['start'])
def start_command(message):
    response_text = "Hello! Welcome to this bot!\n\n"
    response_text += "For help, use the command /help."
    bot.reply_to(message, response_text)
    
@bot.message_handler(commands=['help'])
def help_command(message):
    response_text = "Here are the available commands:\n\n"
    response_text += "/start - Start the bot.\n"
    response_text += "/help - Show this help message.\n"
    bot.reply_to(message, response_text)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, message.text)

# Start the bot
bot.infinity_polling()
