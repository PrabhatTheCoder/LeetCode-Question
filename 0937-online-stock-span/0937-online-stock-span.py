class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # While the stack is not empty and the current price is greater or equal to the top of the stack
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack[-1][1]
            self.stack.pop()
        
        # Push current price and its span onto the stack
        self.stack.append((price, span))
        print(self.stack)
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)