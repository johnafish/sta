import os, requests, math

class Stock:
    
    def __init__(self, symbol, date):
        self.symbol = symbol

        if os.environ.get("ALPHAVANTAGE_API_KEY"):
            self.alphavantage_api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
        else:
            raise EnvironmentError("Must set ALPHAVANTAGE_API_KEY")

        self.daily_data = self.get_daily_data()
        self.fiftydayaverage = self.get_moving_average_50(50)
        self.twodayaverage = self.get_moving_average_200(200)
        self.stock_prediction = self.stock_prediction()

    def get_daily_data(self):
        # Send request to alphavantage
        request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}&apikey={1}".format(self.symbol, self.alphavantage_api_key)
        r = requests.get(request_url)
        if r.status_code != 200:
            return False
        
        # Get data from json of successful request
        return r.json()["Time Series (Daily)"]

    def current_price(self):
        request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval=1min&apikey={1}".format(self.symbol, self.alphavantage_api_key)
        r = requests.get(request_url)
        if r.status_code != 200:
            return False

        for key, value in r.json()["Time Series (1min)"].items():
            return float(value["4. close"])

    def get_moving_average(self, timeperiod) : 
        url = "https://www.alphavantage.co/query?function=SMA&symbol="+self.ticker+"&interval=daily&time_period="+timeperiod+"&series_type=low&apikey="+apikey
        data = json.load(urllib.request.urlopen(url))
        return data["Technical Analysis: SMA"][self.date]["SMA"]


    def stock_prediction(self):
        if(self.fiftydayaverage>self.twodayaverage):
            return "buy"
        else:
            return "sell"


if __name__ == '__main__':
    stocks = ["TD.TO", "SHOP.TO", "AAPL"]
    for stock in stocks:
        s = Stock(stock, "2017-04-28")
        print(stock)
        print(s.stock_prediction)
