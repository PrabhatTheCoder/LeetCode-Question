class MinStack:

    # Time Complexity: O(1) for all operations.
    # Space Complexity: O(n) because the stack can store up to n elements but we are not using extra stack to store min_element.

    def __init__(self):
        self.min_ele = None
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min_ele = val
        else:
            if val >= self.min_ele:
                self.stack.append(val)
            elif val <= self.min_ele:
                self.stack.append(2 * val - self.min_ele)
                self.min_ele = val

    def pop(self) -> None:
        if not self.stack:
            return None
        elif self.stack and self.stack[-1] <= self.min_ele:
            self.min_ele = (2*self.min_ele) - self.stack[-1]
            self.stack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        if self.stack[-1] <= self.min_ele:
            return self.min_ele
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_ele