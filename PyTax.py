#! /opt/local/bin python2.7

# Calculates an average purchase price accounting for dividends
# 1. Determine purchase date, get adjusted price
# 2. On each dividend date afterward:
#	- Calculate shares added (dividend * current shares) / market close
#	- Add shares to running total
#	- update average price based on adjusted prices

# Jason Kahn

from datetime import datetime, timedelta
from Loaders import *

purchaseDate = datetime(1988, 1, 1)
saleDate = datetime(2012, 1, 1)
cummulativeShares = 1

prices = Prices()
dividends = Dividends()

purchasePrice = prices.closestClose(purchaseDate).adjClose
averagePurchasePrice = purchasePrice

print "Dividend date, cummulative shares, new shares purchased, new average purchase price"

for date in sorted(dividends.iterkeys()):
	if ((date < purchaseDate) or (date > saleDate)):
		continue
	newSharesPurchased = (dividends[date] / prices[date].close) * cummulativeShares
	newCummulativeShares = cummulativeShares + newSharesPurchased
	averagePurchasePrice = ((cummulativeShares / newCummulativeShares) * averagePurchasePrice) + ((newSharesPurchased / newCummulativeShares) * prices[date].adjClose)
	cummulativeShares = newCummulativeShares
	print "{0},{1},{2},{3}".format(date, cummulativeShares, newSharesPurchased, averagePurchasePrice)

print "Average purchase price: ", averagePurchasePrice