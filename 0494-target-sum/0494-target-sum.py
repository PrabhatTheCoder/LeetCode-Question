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

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        # Exactly same Question -> https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1
        
        # condition check
        if (total_sum + target) % 2 != 0 or total_sum < target:
            return 0
        
        target_sum = (total_sum + target) // 2
        
        if target_sum < 0:  
            return 0

        return self.isSubsetSum(nums, target_sum)
