#!/usr/bin/env python3
from alpha_vantage.timeseries import TimeSeries
import sys
import random
import json
import os
import pandas as pd
import alertBot as bot
import csv
from dotenv import load_dotenv

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


def getKey():
    """This function returns a random key from the file that contains the API keys"""
    load_dotenv()
    keys = os.getenv('KEYS')
    keys1 = keys.split(' ')
    return random.choice(keys1)


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

# def getStockChangeThreshold(symbol):
#     """This function returns the change threshold for a stock symbol"""
#     stocks = readStocksFromFile('stocks')
#     for stock in stocks:
#         if stock.symbol == symbol:
#             return stock.ct


def getStockData(stock_file):
    """This function calls the Alpha Vantage API to get the stock data in pandas format"""
    stocks = readStocksFromFile(stock_file)
    key = getKey()
    time = TimeSeries(key=key, output_format='pandas')
    pd.set_option('display.max_rows', 500)
    stock_data = []

    for stock in stocks:
        data = time.get_intraday(
            symbol=stock.symbol, interval=time_interval, outputsize='full')
        stock_data.append(data)

    return list(stock_data)


def calculate(data_frame, symbol, ct):
    latest_quote = data_frame[0]['4. close'][0]
    before_quote = data_frame[0]['4. close'][1]
    print(before_quote)
    print(latest_quote)

    loss = False

    # change_in_price = latest_quote - before_quote
    # if change_in_price < 0:
    #     percent = ((change_in_price * -1) / latest_quote) * 100
    #     loss = True
    #     if(percent >= ct):
    #         string = f'The stock {symbol} has fallen below {ct}%. The current price is {latest_quote}'
    #         bot.sendMessage(string)

    # elif change_in_price > 0:
    #     percent = (change_in_price / latest_quote) * 100
    #     loss = False
    #     if(percent >= ct):
    #         string = f'The stock {symbol} has increased above {ct}%. The current price is {latest_quote}'
    #         bot.sendMessage(string)


# data = getStockData('stocks', 'keys')
# for data1 in data:
#     print(data1)

# I need to get the first and second value from the pandas DataFrame -- RECHECK
# I need to get the change threshold percentage -- DONE
# I need to calculate the difference and check if its greater than or less than the CT -- RECHECK
# I need to send the appropriate response to the discord bot -- DONE, need to clean up the exit process

# bot.sendMessage("this is a test from another python script")


stock_objects = readStocksFromFile('stocks')
dt2 = getStockData('stocks')
dt = dt2[0]
print(dt[0]['4. close'])
# print(type(dt2))

calculate(list(dt2[0]), stock_objects[0].symbol,stock_objects[0].ct)  # example of calling this method
