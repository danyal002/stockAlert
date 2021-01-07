import stockAlert as sa
import alertBot as bot

stock_list = sa.getStockData('stocks')
stock_objects = sa.readStocksFromFile('stocks')

for stock, obj in stock_list, stock_objects:
    sa.calculate(stock, obj.symbol, obj.ct)
