class StockSpanner:

    def __init__(self):
        # we will maintain a decreasing stack (bottom - top)
        # we will store stock price + number of days at which it was smaller
        
        # 1, 60
        # 2, 70
        # 1, 80
        # 1, 100
        self.stack = []

    def next(self, price: int) -> int:
        days = 0
        while self.stack and self.stack[-1][1] <= price:
            prev_days, cost = self.stack.pop()
            days += prev_days
        
        days += 1
        self.stack.append((days, price))
        return days
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

#
#
#
#
# (3, 1)
# (2, 2)
# (1, 7)