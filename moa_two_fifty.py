from strategy import Strategy
from stock import Stock

class MoaTwoFifty(Strategy):
    def decision(self, stock):
        # Compare 50 and 200 day averages. 
        # If 50 is greater, bullish -> buy
        # If 200 is greater, bearish -> sell

        two_hundred_day_average = stock.get_moving_average(200)
        fifty_day_average = stock.get_moving_average(50)

        if (fifty_day_average > two_hundred_day_average):
            return 1
        elif (fifty_day_average < two_hundred_day_average):
            return -1
        else:
            return 0

if __name__ == '__main__':
    strategy = MoaTwoFifty()
    stock = Stock("SHOP.TO", "2017-04-28")
    decision = strategy.decision(stock)
    print(decision)
