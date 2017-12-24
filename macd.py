from strategy import Strategy
from stock import Stock


class MACD(Strategy): 

    def decision(self, stock): 
        #checks bullish or bearish trend 
        #if macd>0: bullish trend
        macd_val = float(stock.get_macd_line(stock.date, "macd"))
        signal_val = float(stock.get_macd_line(stock.date,"signal")) 

        #get previous macd and signal line to compare slope
        parsed_date = int(stock.date[8:])-1
        rest_date = (stock.date[0:8])
        macd_sec_val = float(stock.get_macd_line(rest_date+str(parsed_date), "macd")) 
        signal_sec_val = float(stock.get_macd_line(rest_date+str(parsed_date), "signal"))
       
        if (macd_val>signal_val and macd_sec_val<signal_sec_val):
           return 1
           #theoretical upward trend
           #check if macd line crossed signal line 
        elif(macd_val<signal_val and macd_sec_val>signal_sec_val): 
           return -1 

        elif(macd_val>0 and macd_sec_val<0): 
            return 1
        elif(macd_val<0 and macd_sec_val>0): 
            return -1

        else: 
            return 0


if __name__ == '__main__':
    strategy = MACD()
    stock = Stock("SHOP.TO", "2017-04-28")
    decision = strategy.decision(stock)
    print(decision)
        
    
