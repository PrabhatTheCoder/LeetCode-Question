class MyCircularQueue:

    def __init__(self, k: int):
        self.curr_size = 0
        self.capacity = k
        self.back = 0
        self.front = 0
        self.dequeue = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.curr_size == self.capacity:
            return False
        self.dequeue[self.back] = value
        self.back = (self.back + 1) % self.capacity
        self.curr_size += 1
        return True

    def deQueue(self) -> bool:
        if self.curr_size == 0:
            return False
        self.front = (self.front + 1) % self.capacity
        self.curr_size -= 1
        return True

    def Front(self) -> int:
        if self.curr_size == 0:
            return -1
        return self.dequeue[self.front]

    def Rear(self) -> int:
        if self.curr_size == 0:
            return -1
        return self.dequeue[(self.back - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.curr_size == 0

    def isFull(self) -> bool:
        return self.curr_size == self.capacity

# Test Case
# obj = MyCircularQueue(3)
# print(obj.enQueue(2))    # True
# print(obj.Rear())        # 2
# print(obj.Front())       # 2
# print(obj.deQueue())     # True
# print(obj.Front())       # -1
# print(obj.deQueue())     # False
# print(obj.Front())       # -1
# print(obj.enQueue(4))    # True
# print(obj.enQueue(2))    # True
# print(obj.enQueue(2))    # True
# print(obj.enQueue(3))    # False
