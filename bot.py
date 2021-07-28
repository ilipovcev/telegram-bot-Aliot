from Person import Person
from Tesla import Tesla
import telebot
import config
import datetime 

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
markupMain = types.ReplyKeyboardMarkup(resize_keyboard=True)
itemMain1 = types.KeyboardButton("Посмотреть баланс")
itemMain2 = types.KeyboardButton("Портфолио")
markupMain.add(itemMain1, itemMain2)

@bot.message_handler(commands=['start'])
def welcome(message):
	person = Person(message.chat.id, message.chat.username)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markupMain)

@bot.message_handler(content_types=['text'])
def send(message):
	if message.chat.type == 'private':
		if message.text == "Посмотреть баланс":
			bot.send_message(message.chat.id, 'Ваш баланс: ' + str(person.get_balance()) + '$.')
		elif message.text == "Портфолио":
			# Btn in msg
			# markup = types.InlineKeyboardMarkup(row_width=2)
			# item1 = types.InlineKeyboardButton("+2", callback_data='pTwo')
			# item2 = types.InlineKeyboardButton("+5", callback_data='pFive')
			# markup.add(item1, item2)
			person = Person(message.chat.id, message.chat.username)
			print(person.get_portfolio())
		else:
			bot.send_message(message.chat.id, '...')

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

