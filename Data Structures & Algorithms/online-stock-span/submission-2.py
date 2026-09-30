class StockSpanner:

    def __init__(self):
        self.prices = []
        self.index = 0


    def next(self, price: int) -> int:
        self.index += 1
        while self.prices and self.prices[-1][0] <= price:
            self.prices.pop()
        
        span = self.index - self.prices[-1][1] if self.prices else self.index
        self.prices.append((price, self.index))
        return span
    
    # 75,  6
    # 80,  2
    # 100, 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)