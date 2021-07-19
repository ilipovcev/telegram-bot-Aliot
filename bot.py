import telebot
import config
import urllib.request, json
from datetime import datetime 

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

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
			resp = urllib.request.urlopen('https://query2.finance.yahoo.com/v10/finance/quoteSummary/tsla?modules=price')
			data = json.loads(resp.read())
			price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
			print(price)

			dt_now = datetime.now()
			date_time = dt_now.strftime("%d/%m/%Y, %H:%M:%S")

			bot.send_message(message.chat.id, 'Цена на ' + str(date_time) +': ' + str(price) + '$.')
		elif message.text == "Купить акции Tesla":
			# Btn in msg
			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
			item2 = types.InlineKeyboardButton("Плохо", callback_data='bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'Goood', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, '...')

# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
# 	try:
# 		if call.message:
# 			if call.data == 'good':
# 				bot.send_message(call.message.chat.id, 'Awesome')
# 			elif call.data == 'bad':
# 				bot.send_message(call.message.chat.id, 'Sad')
# 	except Exception as e:
# 		print(repr(e))

bot.polling(none_stop=True)

