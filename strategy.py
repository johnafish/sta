class Strategy:
    def decision(self, stock):
        #Returns -1 if sell, 0 if hold, 1 if buy
        raise NotImplementedError
