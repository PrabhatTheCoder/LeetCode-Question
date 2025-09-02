class Solution:
    def solve(self, n, dp):
        if n == 0:
            dp[0] = 0
            return dp[0]
        if n == 1:
            dp[1] = 1
            return dp[1]
        if n == 2:
            dp[2] = 1
            return dp[2]
        if dp[n] != 0:
            return dp[n]
        
        dp[n] = self.solve(n-1, dp) + self.solve(n-2, dp) + self.solve(n-3, dp)
        return dp[n]
        

    def tribonacci(self, n: int) -> int:
        dp = [0] * (n + 1)
        return self.solve(n, dp)
        