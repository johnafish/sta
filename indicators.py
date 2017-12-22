import urllib.request
import json

apikey = "R1OZ339ORWVQ05E9"

class Indicators: 

    def __init__(self,ticker,date):
        self.ticker = ticker
        self.date = date
        self.fiftydayaverage = self.get_moving_average_50()
        self.twodayaverage = self.get_moving_average_200()
        self.stock_prediction = self.stock_prediction()


    def get_moving_average_50(self): 
        url = "https://www.alphavantage.co/query?function=SMA&symbol="+self.ticker+"&interval=daily&time_period=50&series_type=low&apikey="+apikey
        data = json.load(urllib.request.urlopen(url))
        return data["Technical Analysis: SMA"][self.date]["SMA"]

    def get_moving_average_200(self): 
        url = "https://www.alphavantage.co/query?function=SMA&symbol="+self.ticker+"&interval=daily&time_period=200&series_type=low&apikey="+apikey
        data = json.load(urllib.request.urlopen(url))
        return data["Technical Analysis: SMA"][self.date]["SMA"]


    def get_price(self):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+self.ticker+"&apikey="+apikey
        data = json.load(urllib.request.urlopen(url))
        return data["Time Series (Daily)"]

    def stock_prediction(self):
        if(self.fiftydayaverage>self.twodayaverage):
            return "buy"
        else:
            return "sell"



stock1 = Indicators("SHOP", "2017-04-28")
print(stock1.stock_prediction)
