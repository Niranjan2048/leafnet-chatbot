import os
import telebot
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hello, I am a bot")

@bot.message_handler(content_types=['photo'])
def hey(message):
    import requests
    file_info = bot.get_file(message.photo[-1].file_id)

    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_KEY, file_info.file_path))
    if file.status_code == 200:
        with open("D:/Athul/photos/sample.jpg", 'wb') as f:
            f.write(file.content)
    elif file.status_code == 404:
        bot.reply_to(message,"Resend your photo")

    
    bot.reply_to(message, "Hey, I got your photo")


bot.polling()