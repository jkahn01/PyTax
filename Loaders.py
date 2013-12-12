import re, csv
from datetime import datetime, timedelta

price_file = 'price.data'
dividend_file = 'div.data'

non_decimal = re.compile(r'[^\d.]+')

class Prices (dict):
	
	def __init__ (self):
		lines = csv.reader(open(price_file, 'rb'))
		for line in lines:
			if (re.match('a', line[0])):
				date = datetime.fromtimestamp(int(non_decimal.sub('', line[0])))
				lastAbsoluteDate = date
				self._addLine(date, line)
			elif (re.match('\d', line[0])):
				date = lastAbsoluteDate + timedelta(days=(int(line[0])*7))
				self._addLine(date, line)
	
	def _addLine (self, date, line):
		self[date] = line[1]

class Dividends (dict):

	def __init__ (self):
		lines = open(dividend_file, 'rb')
		for line in lines:
			date, div = line.split('$')
			div = float(non_decimal.sub('', div))
			date = datetime.strptime(date, '%b %d, %Y ')
			self[date] = div
		
if __name__ == '__main__':
	dl = Dividends()
	pl = Prices()
	for k in sorted(pl.iterkeys()):
		print k, pl[k]
	for k in sorted(dl.iterkeys()):
		print k, dl[k]
	