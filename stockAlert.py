#!/usr/bin/env python3
from alpha_vantage.timeseries import TimeSeries
import sys
import random
import json
import pandas as pd

# ticker = str(sys.argv[1])

# lines = open('keys').read().splitlines()
# key = lines[0]


# time = TimeSeries(key=key, output_format='pandas')
# data = time.get_intraday(symbol=ticker, interval='30min', outputsize='full')

# print(ticker)
# print(data)

# there are choices between 1min, 15min, 30min & 60min.
time_interval = '60min'


class Stock:
    """This class creates a stock objects using 2 properties, the symbol of the security and the change threshold (in percent)."""

    def __init__(self, symbol, ct):
        self.symbol = symbol
        self.ct = ct


def getKey(file):
    keys = open(file).read().splitlines()
    return random.choice(keys)


def readStocksFromFile(file):
    """This function returns a list of Stock objects after reading them from a file. The 'file' parameter takes in a string which is the name/path of the file."""
    stock_list = []
    with open(file) as stocks:
        stock_list = stocks.read().splitlines()

    refined_list = []
    for stock in stock_list:
        temp = stock.split()
        new_item = Stock(temp[0], temp[1])
        refined_list.append(new_item)

    return refined_list


def getStockData(stock_file, key_file):
    stocks = readStocksFromFile(stock_file)
    key = getKey(key_file)
    time = TimeSeries(key=key, output_format='pandas')
    pd.set_option('display.max_rows', 500)
    stock_data = []

    for stock in stocks:
        data = time.get_intraday(
            symbol=stock.symbol, interval=time_interval, outputsize='compact')
        stock_data.append(data)

    return stock_data


data = getStockData('stocks', 'keys')
for data1 in data:
    print(data1)
