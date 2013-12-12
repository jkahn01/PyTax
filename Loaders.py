import csv
from datetime import datetime, timedelta

price_file = 'prices.csv'
dividend_file = 'dividends.csv'

non_decimal = re.compile(r'[^\d.]+')

class Price: pass

class Prices (dict):
	
	def __init__ (self):
		lines = csv.reader(open(price_file, 'rU'))
		for line in lines:
			try:
				self._addLine(line)
			except:
				continue
	
	def _addLine (self, line):
		date = line[0]
		date = datetime.strptime(date, '%m/%d/%y')
		if (date > datetime.now()):
			date = datetime(date.year-100, date.month, date.year)
		close = float(line[4])
		adjClose = float(line[6])
		self[date] = Price()
		self[date].close= close
		self[date].adjClose = adjClose

class Dividends (dict):

	def __init__ (self):
		lines = csv.reader(open(dividend_file, 'rU'))
		for line in lines:
			try:
				date = line[0]
				date = datetime.strptime(date, '%m/%d/%y')
				if (date > datetime.now()):
					date = datetime(date.year-100, date.month, date.year)
				div = float(line[1])
				self[date] = div
			except:
				continue
		
if __name__ == '__main__':
	dl = Dividends()
	pl = Prices()
	for k in sorted(pl.iterkeys()):
		print k, pl[k].close, pl[k].adjClose
	for k in sorted(dl.iterkeys()):
		print k, dl[k]
	