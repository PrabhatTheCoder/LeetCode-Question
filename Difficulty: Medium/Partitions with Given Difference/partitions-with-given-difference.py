class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
    
        for i in range(n + 1):
            dp[i][0] = 1  # empty subset always possible
    
        for i in range(1, n + 1):
            for j in range(target + 1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
    
        return dp[n][target]

    def countPartitions(self, arr, d):
        total_sum = sum(arr)
        
        # condition check
        if (total_sum + d) % 2 != 0 or total_sum < d:
            return 0
        
        target = (total_sum + d) // 2
        return self.isSubsetSum(arr, target)
