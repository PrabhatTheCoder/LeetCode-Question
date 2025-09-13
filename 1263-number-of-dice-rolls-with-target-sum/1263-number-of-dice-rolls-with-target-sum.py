MOD = 10**9 + 7

class Solution:

    # Recursion  + Memoisation
    
    def solve(self, n, k, target):

        if n == 0 and target == 0:
            return 1
        if n == 0 or target < 0:
            return 0
        
        if self.dp[n][target] != -1:
            return self.dp[n][target]
        
        ways = 0
        for i in range(1,k+1):
            ways += self.solve(n-1, k, target - i) 

        self.dp[n][target] = ways % MOD
        return self.dp[n][target]

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.dp = [[-1] * (target+1) for i in range(n+1)]
        return self.solve(n,k,target)
        
