from stock import Stock

class Position:
    def __init__(self, symbol, quantity, avg_price):
        self.symbol = symbol
        self.quantity = quantity
        self.avg_price = avg_price
        self.stock = Stock(symbol)

    def open_pnl(self):
        return (self.stock.current_price() - self.avg_price) * self.quantity

if __name__ == '__main__':
    td = Position("TD.TO", 13, 73.95)
    shop = Position("SHOP.TO", 10, 133.93)
    print(td.open_pnl()+shop.open_pnl())
