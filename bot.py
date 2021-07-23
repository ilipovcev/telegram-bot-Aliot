from Wallet import Wallet
from Tesla import Tesla
import telebot
import config
import urllib.request, json
from datetime import datetime 

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
wallet = Wallet()

@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Цена акции Tesla")
	item2 = types.KeyboardButton("Купить акции Tesla")

	markup.add(item1, item2)
	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send(message):
	if message.chat.type == 'private':
		if message.text == "Цена акции Tesla":
			dt_now = datetime.now()
			date_time = dt_now.strftime("%d/%m/%Y, %H:%M:%S")

			markup = types.InlineKeyboardMarkup(row_width=1)
			item1 = types.InlineKeyboardButton("Купить", callback_data='buy')
			markup.add(item1)

			bot.send_message(message.chat.id, 'Цена на ' + str(date_time) +': ' + str(Tesla.get_price()) + '$.', reply_markup=markup)
		elif message.text == "Купить акции Tesla":
			# Btn in msg
			# markup = types.InlineKeyboardMarkup(row_width=2)
			# item1 = types.InlineKeyboardButton("+2", callback_data='pTwo')
			# item2 = types.InlineKeyboardButton("+5", callback_data='pFive')
			# markup.add(item1, item2)

			bot.send_message(message.chat.id, f'Ваш баланс: {wallet.get_balance()}')
			bot.send_message(message.chat.id, 'Введите количество акций для покупки')
			bot.register_next_step_handler(message, get_amount_to_buy)
		else:
			bot.send_message(message.chat.id, '...')


def get_amount_to_buy(message):
	if message.text.isdigit() != True:
		print('string')
		return
	tsl = Tesla()
	tsl.buy(int(message.text), wallet)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'pTwo':
				bot.send_message(call.message.chat.id, 'Awesome')
			elif call.data == 'pFive':
				bot.send_message(call.message.chat.id, 'Sad')
	except Exception as e:
		print(repr(e))

bot.polling(none_stop=True)

