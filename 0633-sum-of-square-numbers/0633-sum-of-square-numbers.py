import math

class Solution:

    def perfectSquare(self, val):
        if val < 0:  # Negative numbers cannot be perfect squares
            return False
        root = int(math.sqrt(val))
        return root * root == val

    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(math.sqrt(c))  # Start from the square root of `c`

        while low <= high:
            current_sum = low * low + high * high
            if current_sum == c:
                return True
            elif current_sum < c:
                low += 1
            else:
                high -= 1

        return False
