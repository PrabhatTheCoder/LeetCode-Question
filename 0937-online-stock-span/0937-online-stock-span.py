class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []

    def next(self, price: int) -> int:
        span = 1
        while self.prices and self.prices[-1] <= price:
            span += self.stack.pop()
            self.prices.pop()
        self.stack.append(span)
        self.prices.append(price)
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)