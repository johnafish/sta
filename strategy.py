class Strategy:
    def decision(self, stock):
        #Returns float in [-1, 1] where -1 is strong sell and 1 is strong buy (0 being hold)
        raise NotImplementedError
