class Solution:

    def helper(self, cost, n, dp):
        if n >= len(cost):
            return 0
        if dp[n] != -1:
            return dp[n]
        dp[n] = cost[n] + min(self.helper(cost, n+1, dp),
                              self.helper(cost, n+2, dp))
        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*len(cost)
        return min(self.helper(cost, 0, dp), self.helper(cost, 1, dp))
