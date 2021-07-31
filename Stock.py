from PSQL import DataBase
import urllib.request, json

class Stock(object):
	def __init__(self, name):
		self.id = -1
		self.quantity = 0
		self.price = 0
		self.name = name
		self.db = DataBase()

	def get_id(self):
		self.id = self.db.get_stock_id(self.name)
		return self.id

	def get_name(self):
		return self.name

	def set_price(self, price):
		self.price = price

	def get_price(self):
		return self.price

class Tesla(Stock):
	def get_price(self):
		resp = urllib.request.urlopen('https://query2.finance.yahoo.com/v10/finance/quoteSummary/tsla?modules=price')
		data = json.loads(resp.read())
		self.price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
		return self.price