from position import Position

class Portfolio:
    def __init__(self, positions):
        # positions: array of Position objects
        self.positions = positions

    def open_pnl(self):
        self.pnl = 0
        for position in self.positions:
            openpnl = position.open_pnl()
            print(openpnl)
            self.pnl += openpnl
        return self.pnl

    def total_cost(self):
        self.cost = 0
        for position in self.positions:
            self.cost += position.total_cost()
        return self.cost

    def current_value(self):
        self.value = 0
        for position in self.positions:
            self.value += position.current_value()
        return self.value

if __name__ == '__main__':
    p = Portfolio([Position("TD.TO", 13, 73.95), Position("SHOP.TO", 10, 133.93), Position("POW.TO", 5, 32.39)])
    print(p.total_cost())
    print(p.current_value())

