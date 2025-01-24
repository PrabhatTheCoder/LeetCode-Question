class Solution:
    def climbStairs(self, n: int,  memo={}) -> int:
        if n in memo:  # Check if result is already computed
            return memo[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]
        