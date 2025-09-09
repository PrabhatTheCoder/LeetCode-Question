class Solution:
    def solve(self, price, n, dp):
        # base case
        if n == 0:
            return 0

        if dp[n] != -1:
            return dp[n]

        max_val = float('-inf')

        # try all possible cuts
        for i in range(1, n+1):
            max_val = max(max_val, price[i-1] + self.solve(price, n-i, dp))

        dp[n] = max_val
        return dp[n]

    def cutRod(self, price):
        n = len(price)
        dp = [-1] * (n+1)
        return self.solve(price, n, dp)
