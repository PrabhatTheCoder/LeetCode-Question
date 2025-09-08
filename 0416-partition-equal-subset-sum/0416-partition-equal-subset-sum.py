class Solution:

    def isSubsetSum(self, arr, target):
        n = len(arr)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
    
        for i in range(n + 1):
            dp[i][0] = True
    
        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i-1] <= j:
                    # include arr[i-1] OR exclude it
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    # can't include arr[i-1]
                    dp[i][j] = dp[i-1][j]
    
        return dp[n][target]

    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        if sum%2 != 0:
            return False
        return self.isSubsetSum(nums, sum//2)
        