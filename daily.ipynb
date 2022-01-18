# QuantConnect
# Back test MA Crossover alpha
# Run this cell first
from clr import AddReference
AddReference("System")
AddReference('System.Memory')
AddReference("QuantConnect.Common")
AddReference("QuantConnect.Research")
AddReference("QuantConnect.Indicators")
from System import *
from QuantConnect import *
from QuantConnect.Data.Market import TradeBar, QuoteBar
from QuantConnect.Research import *
from QuantConnect.Indicators import *
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import math

# begin define common class

class ExitSignalSystem:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.qb = QuantBook()
        _equity = self.qb.AddEquity(symbol)
        self.asset = self.qb.History(_equity.Symbol, start_date, end_date, Resolution.Daily)
        
    def get_stop_loss_price(self, stop_loss_rate):
        recent_highest_price = max(self.asset.loc[self.symbol]['high'])
        return recent_highest_price * (1-stop_loss_rate)
        

class SimpleBuySystem:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.qb = QuantBook()
        _equity = self.qb.AddEquity(symbol)
        self.asset = self.qb.History(_equity.Symbol, start_date, end_date, Resolution.Daily)
        
    def get_recent_high_price(self, period, threshold=1):
        i=-1*period
        res=0
        while i<0:
            if (self.asset.iloc[i]['open']-self.asset.iloc[i]['close'])/self.asset.iloc[i]['open']>=threshold:
                res=self.asset.iloc[i]['close']
            else:
                res=max(res, self.asset.iloc[i]['high'])
            i+=1
        return res
        # return max(self.asset.iloc[-1*period:]['high'])
    
    def get_target_price(self, purchase_price, target_rate):
        cur_price = self.asset.loc[self.symbol].iloc[-1]['close']
        r = math.ceil(math.log(cur_price / purchase_price) / math.log(1+target_rate))
        # print(self.asset.loc[self.symbol])
        if r > 0:
            return purchase_price * pow((1+target_rate), r), purchase_price * pow((1+target_rate), r-1)
        else:
            return purchase_price, 0
   
    
# end define common class
    
# daily predition
assets = [
    {'symbol':'VOO', "purchase_price":0, "purchase_date":"", "target_rate":0.05, "buy_threshold":0.02}, 
    {'symbol':'MGK', "purchase_price":0, "purchase_date":"", "target_rate":0.05, "buy_threshold":0.02},
    #{'symbol':'VOO', "purchase_price":421.50, "purchase_date":"2021-11-30", "target_rate":0.016, "buy_threshold":0.017},       
    # {'symbol':'VTV', "purchase_price":140.74, "purchase_date":"2021-06-03", "target_rate":0.016, "buy_threshold":0.015},    
    #{'symbol':'AMZN', "purchase_price":3461.24, "purchase_date":"2021-12-10", "target_rate":0.034, "buy_threshold":0.036},
    #{'symbol':'GOOG', "purchase_price":2926, "purchase_date":"2021-11-22", "target_rate":0.027, "buy_threshold":0.030},
    #{'symbol':'MSFT', "purchase_price":331.36, "purchase_date":"2021-11-23", "target_rate":0.025, "buy_threshold":0.028},
    #{'symbol':'MGK', "purchase_price":257, "purchase_date":"2021-11-30", "target_rate":0.020, "buy_threshold":0.02},
]
start_date =datetime.today() - timedelta(days=20)
end_date = datetime.now()
look_back_periods = 10
stop_loss_rate = 0.01

#target_rate = 0.02
#buy_threshold = 0.015

for asset in assets:
    sh = SimpleBuySystem(asset['symbol'], start_date, end_date)
    target_rate = asset['target_rate']
    buy_threshold = asset['buy_threshold']
    recent_high = sh.get_recent_high_price(look_back_periods, buy_threshold / 2)
    
    if asset['purchase_date'] != '' and asset['purchase_date'] is not None:
        _pur_date = datetime.strptime(asset['purchase_date'], "%Y-%m-%d")
        target_price, stop_price = sh.get_target_price(asset['purchase_price'], target_rate)
        if stop_price == 0:
            stop_price = asset['purchase_price'] * ( 1 - stop_loss_rate)
        
        if (end_date - _pur_date).days >= 5:
            s2 = ExitSignalSystem(asset['symbol'], _pur_date, end_date)
            stop_loss_price = s2.get_stop_loss_price(buy_threshold/2)
            stop_loss = 'Stop Loss = {0:.2f}, Exit Price = {1:.2f}'.format(stop_price, stop_loss_price)            
        else:
            stop_loss = 'No Exit yet'
        print('{0} Target={1:.2f}, {2}'.format(asset['symbol'].ljust(10), target_price, stop_loss))
    else:
        print('{0} Recent High Price = {1:.2f}, buy threshold = {2:.2f}'.format(asset['symbol'].ljust(10), recent_high, recent_high*(1-buy_threshold)))
