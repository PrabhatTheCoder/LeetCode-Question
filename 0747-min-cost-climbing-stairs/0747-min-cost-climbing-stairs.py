from typing import List

class Solution:

    def helper(self, cost, n, dp):
        if n < 0: 
            return 0
        if n == 0 or n == 1:
            return cost[n]
        if dp[n] != -1:
            return dp[n]
        dp[n] = cost[n] + min(self.helper(cost, n-1, dp),
                              self.helper(cost, n-2, dp))
        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n
        return min(self.helper(cost, n-1, dp), self.helper(cost, n-2, dp))
