# Tradebook class

from ast import Num
from typing import Dict



class Tradebook():
    # array of positions that are currently open and held
    openTrades = {}
    # array of all closed trades, i.e. previously held and now sold
    closedTrades = {}
    # array of orders
    all_orders = []
    totalProfit = 0
    
    def __init__():
        pass
    def __str__(self):
        pass
    
    # Set Methods
    def add_open_trade(self, order):
        self.openTrades.append(order)
        
    def add_closed_trade(self, order):
        pass
    
    # Get methods
    def get_order_history(self):
        return all_orders
    

        
        
            
class Order():
    def __init__(self, symbol, open, open_date, pl=None, close=None, close_date=None, closed=False):
        self.symbol = symbol
        self.open = open # price bought at
        self.open_date = open_date # start date
        self.close = close # price sold at
        self.pl = pl # profit/loss
        self.close_date = close_date # end date
        self.closed = closed # status - open or closed
        
        
    # Params (closing price: Double, closing date: Post)
    def close_order(self, close, close_date):
        if self.closed == False and ((self.date_convert(close_date) - self.date_convert(self.open_date)) > 0):
            if self.close == None and self.close_date == None:
                self.close = close
                self.closed = True
                self.close_date = close_date

