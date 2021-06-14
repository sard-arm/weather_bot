import telebot
import network

API_TOKEN = "1766208048:AAFY6rVTYsUVQy9fIPSqLlqsDFdv3zWgS5M"
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    answer = "Hello"
    bot.send_message(chat_id=message.chat.id, text=answer)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    city_name = message.text
    temp = network.weather(city_name)
    if temp is None:
        answer = "City not found:("
    else:
        answer = "Temperature in %s: %d" % (city_name, temp)
    bot.send_message(message.chat.id, answer)

bot.polling()


