import os, requests, math

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol

        if os.environ.get("ALPHAVANTAGE_API_KEY"):
            self.alphavantage_api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
        else:
            raise EnvironmentError("Must set ALPHAVANTAGE_API_KEY")

        self.daily_data = self.get_daily_data()

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
            return value["4. close"]

    def rolling_avg(self, num_days):
        if not self.daily_data:
            self.get_daily_data()

        days = 0
        average_close_price = 0
        for key, value in self.daily_data.items():
            if days == num_days:
                break
            average_close_price += float(value["4. close"])
            days += 1
        average_close_price /= days
        return average_close_price

    def rolling_stdev(self, num_days):
        if not self.daily_data:
            self.get_daily_data()

        mean = self.rolling_avg(num_days)
        days = 0
        stdev = 0
        for key, value in self.daily_data.items():
            if days == num_days:
                break
            stdev += (float(value["4. close"])-mean)**2
            days += 1
        stdev = math.sqrt(stdev/days)
        return stdev

if __name__ == '__main__':
    stocks = ["TD.TO", "SHOP.TO", "AAPL"]
    for stock in stocks:
        s = Stock(stock)
        print(stock)
        print(s.current_price())
        print(s.rolling_avg(30))
        print(s.rolling_stdev(30))
