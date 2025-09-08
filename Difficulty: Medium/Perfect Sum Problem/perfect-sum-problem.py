# User function Template for python3
MOD = 10**9 + 7

class Solution:
    
    def isSubsetSum(self, arr, target):
        n = len(arr)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
    
        # Base case: there is always 1 subset (empty subset) with sum = 0
        for i in range(n + 1):
            dp[i][0] = 1
    
        # Fill DP table
        for i in range(1, n + 1):
            for j in range(0, target + 1):
                if arr[i-1] <= j:
                    # include arr[i-1] OR exclude it
                    dp[i][j] = (dp[i-1][j-arr[i-1]] + dp[i-1][j]) % MOD
                else:
                    # can't include arr[i-1]
                    dp[i][j] = dp[i-1][j] % MOD
    
        return dp[n][target]
        
    def perfectSum(self, arr, target):
        return self.isSubsetSum(arr, target)
