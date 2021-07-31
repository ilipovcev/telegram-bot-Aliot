from Person import Person
import telebot
import config
import datetime
import Stock

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

markupMain = types.ReplyKeyboardMarkup(resize_keyboard=True)
itemMain1 = types.KeyboardButton("Посмотреть баланс")
itemMain2 = types.KeyboardButton("Портфолио")
markupMain.add(itemMain1, itemMain2)

person = Person()

@bot.message_handler(commands=['start'])
def welcome(message):
	person.set_person(message.chat.id, message.chat.username)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markupMain)

@bot.message_handler(commands=['sell'])
def sell_message(message):
	person.set_person(message.chat.id, message.chat.username)
	person.sold_stock(1, Stock.Tesla('TSLA'))

@bot.message_handler(commands=['buy'])
def sell_message(message):
	person.set_person(message.chat.id, message.chat.username)
	if person.buy_stock(1, Stock.Tesla('TSLA')) == -1:
		bot.send_message(message.chat.id, "Недостаточно средств")

@bot.message_handler(content_types=['text'])
def send(message):
	person.set_person(message.chat.id, message.chat.username)
	if message.chat.type == 'private':
		if message.text == "Посмотреть баланс":
			bot.send_message(message.chat.id, 'Ваш баланс: ' + str(person.get_balance()) + '$.')
		elif message.text == "Портфолио":
			# Btn in msg
			# markup = types.InlineKeyboardMarkup(row_width=2)
			# item1 = types.InlineKeyboardButton("+2", callback_data='pTwo')
			# item2 = types.InlineKeyboardButton("+5", callback_data='pFive')
			# markup.add(item1, item2)
			portfolio = person.get_portfolio()
			for part in portfolio:
				bot.send_message(message.chat.id, f'Название: {part[0]}\nКоличество: {part[1]}\nВложенно средств: {part[2]}$')
		else:
			bot.send_message(message.chat.id, 'Неизвестная команда')

bot.polling(none_stop=True)

