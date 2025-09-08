class Solution:
    
    
    # Bottom Up
    def solve(self, nums, i, target):

        if target == 0:
            return True

        if i < 0:
            return False
        
        # If current element is greater than target, skip it
        if nums[i] > target:
            return self.solve(nums, i-1, target)

        select = self.solve(nums, i-1, target - nums[i])
        not_select = self.solve(nums, i-1, target)
        
        return select or not_select
        
        
    # Top Down Approach
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

               
        # [0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0, 0]
             
            
        # return self.solve(arr, len(arr)-1, target)
