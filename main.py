import stockAlert as sa
import alertBot as bot

stock_list = sa.getStockData('stocks')
stock_objects = sa.readStocksFromFile('stocks')

counter = 0

lst = []
big_string = ''

for stock in stock_list:
    lst.append(sa.calculate(stock, stock_objects[counter].symbol, stock_objects[counter].ct))
    counter += 1

for ms in lst:
    big_string += ms + '\n\n'

print(big_string)
bot.sendMessage(big_string)

# need to configure time libraries so that the script only runs once per hour.