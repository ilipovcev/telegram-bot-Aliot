class Wallet(object):
	def __init__(self):
		self.money = 5000

	def spend_money(self, amount):
		if (self.money - amount) < 0:
			return False
		else:
			self.money -= amount
			return True

	def adding_balance(self, amount):
		self.money += amount

	def get_balance(self):
		return self.money
