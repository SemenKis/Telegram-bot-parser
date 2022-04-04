import telebot
import json
from telebot import types
import caller

bot = telebot.TeleBot('5254316199:AAG0259Rkkzmb179uY6tGW3fSQ8jLy5iBhA')

def read_json(path, chat):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            bot.send_message(chat, item['Date and city'] + ' ' + item["time"] + ' | ' + item["team"] + ' vs ' + item["team_opposite"], parse_mode='')

def menu_buttons():
    kb = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text='MHL', callback_data='mhl')
    button_2 = types.InlineKeyboardButton(text='KHL', callback_data='khl')
    button_3 = types.InlineKeyboardButton(text='SHL', callback_data='shl')
    button_4 = types.InlineKeyboardButton(text='NHL', callback_data='nhl')
    kb.add(button_1, button_2, button_3, button_4)
    return kb

def game_buttons(team):
    kb = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=False, resize_keyboard=True)
    button_1 = types.KeyboardButton(f'{team} playoffs')
    buttons_2 = types.KeyboardButton(f'{team} regular season')
    menu = types.KeyboardButton('menu')
    kb.add(button_1, buttons_2, menu)
    return kb

@bot.message_handler(commands=['start'])
def start(message):
    msg = f'<b>Hi {message.from_user.first_name} {message.from_user.last_name}</b>\ndo you wanna see something 😏? if you want, please send /show command'
    bot.send_message(message.chat.id, msg,parse_mode='html')

@bot.message_handler(commands=['show'])
def show(message):
    bot.send_message(message.chat.id, 'Choose hockey league 🏒🥅', reply_markup=menu_buttons())

@bot.callback_query_handler(func=lambda m: True)
def get_answer(call):
    if call.data == 'mhl':
        bot.send_message(call.message.chat.id, '👍🏻', reply_markup=game_buttons('mhl'))

    if call.data == 'khl':
        bot.send_message(call.message.chat.id, '👍🏻', reply_markup=game_buttons('khl'))

    if call.data == 'shl':
        bot.send_message(call.message.chat.id, '👍🏻', reply_markup=game_buttons('shl'))

    if call.data == 'nhl':
        bot.send_message(call.message.chat.id, '👍🏻', reply_markup=game_buttons('nhl'))

def get_caller(text, chat):
    caller.call_parser(text, chat)

@bot.message_handler(content_types=['text'])
def get_answer(message):
    get_caller(message.text, message.chat.id)
    if message.text == 'menu':
        bot.send_message(message.chat.id, '<b>you can choose again 👇🏻</b>', parse_mode='html', reply_markup=menu_buttons())


bot.polling(none_stop=True)