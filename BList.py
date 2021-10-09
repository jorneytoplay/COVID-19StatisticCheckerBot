import telebot
from telebot import types

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