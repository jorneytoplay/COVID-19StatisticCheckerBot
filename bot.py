import json

import telebot
import ApiConnector
import Key

from telebot import types

country_list = ('ru', 'ua', 'by')
bot = telebot.TeleBot(Key.TOKEN)  # Send security token
ru = types.KeyboardButton('Russia 'u"\U0001F1F7\U0001F1FA")  # Add buttonboard
uk = types.KeyboardButton('Ukraine'u"\U0001F1FA\U0001F1E6")
by = types.KeyboardButton('Belarus'u"\U0001F1E7\U0001F1FE")
cnfrmd = types.KeyboardButton('Confirmed'u"\U0001F468\U0000200D\U00002695\U0000FE0F")  # Add buttonboard
rcvrd = types.KeyboardButton('Recovered'u"\U0001F49B")
dths = types.KeyboardButton('Deaths'u"\U0001FAA6")
crit = types.KeyboardButton('Critical'u"\U0001F641")
bck = types.KeyboardButton('Back'    u"\U0001F519")
latest_info = types.KeyboardButton('Daily Report'u"\U0001F3E5")
all_info = types.KeyboardButton('Total Information'u"\U0001F306")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Create buttonboard
    markup.add(ru, uk, by)
    bot.send_message(message.chat.id, 'Hello, {0.first_name}! Choose a country:'.format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def chose_country(message):
    country = None
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Create buttonboard
    markup.add(ru, uk, by)
    bot.send_message(message.chat.id, 'Choose a country:'.format(message.from_user), #ПОЧЕМУ ТО ВЫЗЫВАЕТСЯ ДВАЖДЫ
                     reply_markup=markup) #1
    if 'Russia' in message.text:
        country = 'ru'

    elif 'Ukraine' in message.text:
        country = 'ua'

    elif 'Belarus' in message.text:
        country = 'by'

    if country not in country_list:
        bot.send_message(message.chat.id, 'Choose a country:'.format(message.from_user),  # ПОЧЕМУ ТО ВЫЗЫВАЕТСЯ ДВАЖДЫ
                         reply_markup=markup)
    else:
        markup.add(latest_info, all_info)
        bot.send_message(message.chat.id,
                         'Choose to receive recent or general country information:'.format(message.from_user),
                         reply_markup=markup)

        if country in country_list:
            bot.register_next_step_handler(message, chose_mode, country) #2


def chose_mode(message, country):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    print(message.text) #ПОЧЕМУ ОН ВЫВОДИТ Russia 🇷🇺 а не Daily    #3
    if 'Daily' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Create buttonboard
        markup.add(cnfrmd, rcvrd, crit, dths, bck)
        bot.send_message(message.chat.id,
                         'Select the information you would like to know:'.format(message.from_user),
                         reply_markup=markup)
        mode = 'daily'
        bot.register_next_step_handler(message, chose_info, country, mode)
    elif 'Total' in message.text:
        print("daaaaa")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Create buttonboard
        markup.add(cnfrmd, rcvrd, crit, dths, bck)
        bot.send_message(message.chat.id,
                         'Select the information you would like to know:'.format(message.from_user),
                         reply_markup=markup)
        mode = 'total'
        bot.register_next_step_handler(message, chose_info, country, mode)

    else:
        bot.send_message(message.chat.id,
                         'Please try again:'.format(message.from_user))
        bot.register_next_step_handler(message, chose_country)


def chose_info(message, country, mode):
    try:
        text = ApiConnector.get_data(country)  # get json info about country
    except:
        bot.send_message(message.chat.id,
                         'An error occurred while getting data, please try again later... 😞'.format(message.from_user))
        print("Cannot connection to API")
    if 'message' not in text:
        if 'Back' in message.text:
            bot.register_next_step_handler(message, chose_country) #4

        if 'Confirmed' in message.text:
            bot.send_message(message.chat.id, text[0]['confirmed'])
            bot.register_next_step_handler(message, chose_info, country)


        elif "Recovered" in message.text:
            bot.send_message(message.chat.id, text[0]['recovered'])
            bot.register_next_step_handler(message, chose_info, country)

        elif 'Deaths' in message.text:
            bot.send_message(message.chat.id, text[0]['deaths'])
            bot.register_next_step_handler(message, chose_info, country)

        elif 'Critical' in message.text:
            bot.send_message(message.chat.id, text[0]['critical'])
            bot.register_next_step_handler(message, chose_info, country)

    else:
        bot.send_message(message.chat.id,
                         "Sorry, the bot is overloaded with requests, please try again in a few seconds... 😞")
        bot.register_next_step_handler(message, chose_info, country)
        print("More requests")


bot.polling(none_stop=True)

if __name__ == '__main__':
    start()
