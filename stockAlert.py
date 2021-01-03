#!/usr/bin/env python3
from alpha_vantage.timeseries import TimeSeries
import sys
import pandas

# ticker = str(sys.argv[1])

# lines = open('keys').read().splitlines()
# key = lines[0]


# time = TimeSeries(key=key, output_format='pandas')
# data = time.get_intraday(symbol=ticker, interval='30min', outputsize='full')

# print(ticker)
# print(data)

class Stock:
    def __init__(self, symbol, ct):
        self.symbol = symbol
        self.ct = ct


def readStocks(file):
    stock_list = []
    with open(file) as stocks:
        stock_list = stocks.read().splitlines()

    refined_list = []
    for stock in stock_list:
        temp = stock.split()
        new_item = Stock(temp[0], temp[1])
        refined_list.append(new_item)

    return refined_list


foo = readStocks('stocks')
for item in foo:
    print(f'{item.symbol} {item.ct}')
