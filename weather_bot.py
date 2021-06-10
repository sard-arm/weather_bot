import telebot
import random
API_TOKEN = '1743525616:AAHKI17GeI8GZp5uti48wq4eLCGGGHW31X0'
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    answer = "Hello"
    bot.send_message(chat_id=message.chat.id, text=answer)
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    answer = "13 *c"
    if message.text == "moscow":
        bot.send_message(message.chat.id, answer)

  

#dsdascscsccca













bot.polling()


