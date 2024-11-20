from flask import Flask, request
import telebot

# Initialize Flask and Telegram Bot
app = Flask(__name__)
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(BOT_TOKEN)

# Command handler for /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to GEN-Z! 🌟 Let's get started.")

# Example text handler
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = f"Hello, {message.from_user.first_name}! This is GEN-Z Mini App!"
    bot.reply_to(message, response)

# Set Webhook for Telegram
@app.route('/' + BOT_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your-app-url.com/' + BOT_TOKEN)
    return "Webhook set!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
