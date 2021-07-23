from Stock import Stock
import urllib.request, json

class Tesla(Stock):
	def get_price(self):
		resp = urllib.request.urlopen('https://query2.finance.yahoo.com/v10/finance/quoteSummary/tsla?modules=price')
		data = json.loads(resp.read())
		self.price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
		return self.price