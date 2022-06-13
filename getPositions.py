from optparse import Option
from telnetlib import DO
from tkinter import END
from tokenize import Double
import alpaca_trade_api as tradeapi
import numpy as np
import time
from alpaca_trade_api.rest import TimeFrame
from datetime import datetime
import collections 
import tradebook



# Resource used: https://github.com/alpacahq/alpaca-trade-api-python



# set up to configure Alpaca api for paper trading account
SEC_KEY = '7OjwTUo67DmXFouuCVXYOL8I4ipHLZ2CAtwhdk7D' # Enter Your Secret Key Here
PUB_KEY = 'PKJ411YIMFUT73HT3ZG7' # Enter Your Public Key Here
BASE_URL = 'https://paper-api.alpaca.markets' # This is the base URL for paper trading
api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL) # For real trading, don't enter a base_url
    
    
print("Hello: let me see what positions you have open")

print("Account status: ")
account = api.get_account()
print("Your account is: " + account.status + ". Your id is: " + account.id + ".")
print("Account funds")
print(account.equity)
print("")


print("Open orders:")
open_orders = api.list_orders()
print(open_orders)
print("")

print("current positions: ")
# unrealized_intraday_pl is pl for the day
# unrealized_pl is total pl
pos_position = api.list_positions()
totalPL = 0
for pos in pos_position:
    
    #self, symbol, open, open_date, pl=None, close=None, close_date=None, closed=False
    
    now = datetime.now()
    symb = pos._raw['symbol']
    qty = pos._raw['qty']
    price = pos._raw['current_price']
    pl = pos._raw['unrealized_pl']
    
    #order = Order(symb, qty, price, pl)
    # add order to the tradebook
    
    # Total pl
    totalPL += float(pl)
    
    print("You own " + str(qty) + " of " + symb)
    print("The current price as of " + str(now) + " is: " + str(price))
    print("Your total Profit/Loss is: " + str(pl))
    print("")
    print("*******************************************************************************")
    print("")
    
print("Your total profit and loss over these positions is: " + str(totalPL))
response = input("Would you like to see more details about your positions?")


while response not in ["y", "Y", "N", "n"]:
    print("Invalid input. Please use \"YyNn\"")
    response = input("")
    
# print organized table with more data - either create your own or use alapacas objects
if response == "y" or response == "Y":
    count = 1
    x = api.get_portfolio_history()
    print("")
    print(x.df)
    print("")
    for pos in pos_position:
        sym = pos._raw["symbol"]
        
        print("Position " + str(count) + ": " + sym +  " -_____________________________________________________-")
        print(pos)
        count += 1
        
elif response == "N" or response =="n":
    pass
else:
    print("Somehow still an invalid response: Quiting")
    exit()

    
# Sell all?
print("")
#liquidate = input("Would you like to liquidate all these positions?")
#if liquidate in ["Y", "y"]:
  #  pass
    



    
    
# Set up logger to help debug and view all activity
"""
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    
"""
