#!/usr/bin/env python3

from alpha_vantage.timeseries import TimeSeries
import sys
import pandas

ticker = str(sys.argv[1])

lines = open('keys').read().splitlines()
key = lines[0]

time = TimeSeries(key=key, output_format='pandas')
data = time.get_intraday(symbol=ticker, interval='30min', outputsize='full')

print(ticker)
print(data)
