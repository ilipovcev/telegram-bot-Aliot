import PSQL as DB

class Person:
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.balance = 5000
		self.db = DB.DataBase()

	def find_user(self):
		return self.db.find_user(self.id, self.name, self.balance)

	def buy_stock(self, amount, Stock):
		stock_price = Stock.get_price()
		if self.get_balance() - (amount * stock_price) >= 0:
			stock_id = self.db.get_stock_id(Stock.get_name())
			self.db.add_stocks(self.id, stock_id, amount, amount * stock_price)

			self.balance -= amount * stock_price
			self.db.update_balance(self.id, self.balance)
			return self.balance
		else:
			return -1

	def sold_stock(self, amount, Stock):
		stock_price_now = Stock.get_price()
		stock_id = self.db.get_stock_id(Stock.get_name())

		stock_price_old = self.db.sold_stock(self.id, stock_id, amount)
		print("Прибыль", stock_price_now / stock_price_old * 100)
		pass

	def get_balance(self):
		self.balance = self.db.get_user_balance(self.id)
		return self.balance

	def get_portfolio(self):
		pass

p = Person(5, 'name')
p.buy_stock(2, 1)