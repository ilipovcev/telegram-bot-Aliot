class Wallet(object):
	def __init__(self):
		self.money = 5000

	def SpendMoney(self, amount):
		if (self.money - amount) < 0:
			return -1
		else:
			self.money -= amount
			return 0

	def AddingBalance(self, amount):
		self.money += amount

	def GetBalance(self):
		return self.money
