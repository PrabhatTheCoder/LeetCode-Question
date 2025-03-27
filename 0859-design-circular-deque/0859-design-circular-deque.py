class MyCircularDeque:

    def __init__(self, k: int):
        self.curr_size = 0
        self.capacity = k
        self.back = 0
        self.front = 0
        self.dequeue = [None] * k
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.back = self.front
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity
        self.dequeue[self.front] = value
        self.curr_size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.back = 0
        else:
            self.back = (self.back + 1) % self.capacity
        self.dequeue[self.back] = value
        self.curr_size += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.back:
            self.front = 0
            self.back = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.curr_size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.back:
            self.front = 0
            self.back = -1
        else:
            self.back = (self.back - 1 + self.capacity) % self.capacity
        self.curr_size -= 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.dequeue[self.front]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.dequeue[self.back]
        

    def isEmpty(self) -> bool:
        return self.curr_size == 0
        

    def isFull(self) -> bool:
        return self.curr_size == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()