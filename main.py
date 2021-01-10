import stockAlert as sa
import alertBot as bot
import datetime
import time


# need to configure time libraries so that the script only runs once per hour.


# # now = datetime.datetime.now()
# print(now.strftime("%H:%M:%S"))
# print(type(now.hour))

# # def checkTime():
# #     now = datetime.datetime.now()
# #     if now.minute == 0 and now.second == 0:
# #         return True

while True:

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

    bot.sendMessage(big_string) 
    time.sleep(10)

# bot.sendMessage("hi idiot")


