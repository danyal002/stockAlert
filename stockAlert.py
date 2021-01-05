#!/usr/bin/env python3
from alpha_vantage.timeseries import TimeSeries
import sys
import random
import json
import pandas as pd
import alertBot as bot

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
    """This function returns a random key from the file that contains the API keys"""
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
    """This function calls the Alpha Vantage API to get the stock data in pandas format"""
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


# data = getStockData('stocks', 'keys')
# for data1 in data:
#     print(data1)


# I need to get the first and second value from the pandas DataFrame
# I need to get the change threshold percentage
# I need to calculate the difference and check if its greater than or less than the CT
# I need to send the appropriate response to the discord bot -- DONE, need to clean up the exit process

bot.sendMessage("this is a test from another python script")
