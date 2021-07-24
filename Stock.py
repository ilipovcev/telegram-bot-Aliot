class Stock(object):
	def __init__(self, name):
			self.quantity = 0
			self.price = 0
			self.name = name

	def get_name(self):
		return self.name

	def set_price(self, price):
		self.price = price

	def get_price(self):
		return self.price