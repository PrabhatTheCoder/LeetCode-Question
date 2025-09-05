class Solution:
    def divisorGame(self, n: int) -> bool:
        if n <= 1:
            return False
        for x in range(1,n):
            if n%x == 0:
                return not self.divisorGame(n-x)
        return False
        