class Stock(object):
	def __init__(self):
			self.quantity = 0
			self.price = 0

	def set_price(self, price):
		self.price = price

	def get_price(self):
		return self.price

	def buy(self, count, Wallet):
		print(Wallet.get_balance())
		if Wallet.spend_money(count * self.get_price()):
			self.quantity += count
		else:
			return False

	def sold(self, count, Wallet):
		if self.quantity - count < 0:
			return False
		else:
			Wallet.adding_balance(Wallet, count * self.get_price())
			self.quantity -= count
			return True

	def get_quantity(self):
		return self.quantity