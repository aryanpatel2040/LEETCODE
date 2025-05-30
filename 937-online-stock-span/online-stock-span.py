class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:
        counter = 1
        while self.stack and self.stack[-1][0] <= price:
            counter += self.stack.pop()[1]

        self.stack.append((price,counter))
        return counter


