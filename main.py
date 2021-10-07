
import telebot
import requests
import Key
from telebot import types
bot = telebot.TeleBot(Key.TOKEN) #Send security token
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #Create buttonboard
    btn1 = types.KeyboardButton('Russia 'u"\U0001F1F7\U0001F1FA") #Add buttonboard
    btn2 = types.KeyboardButton('Ukraine'u"\U0001F1FA\U0001F1E6")
    btn3 = types.KeyboardButton('Belarus'u"\U0001F1E7\U0001F1FE")
    markup.add(btn1,btn2,btn3)
    bot.send_message(message.chat.id,'Hello, {0.first_name}!'.format(message.from_user),reply_markup=markup)

bot.polling(none_stop=True)



def get_data():
    url = "https://covid-19-data.p.rapidapi.com/country/code"

    querystring = {"code": "ua"}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "80f5cd2616msh4cc5ed9bdfe1ae3p12bf84jsnf661f75073ca"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.json())


if __name__ == '__main__':
    start()


