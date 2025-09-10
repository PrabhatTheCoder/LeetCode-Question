# User function Template for python3
class Solution:
    
    # Subset Sum DP (True/False table)
    def isSubsetSum(self, arr, target):
        n = len(arr)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
    
        for i in range(n + 1):
            dp[i][0] = True  
    

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
    
        return dp
    
    def minDifference(self, arr):
        range_sum = sum(arr)
        n = len(arr)
        
        # Get DP table
        dp = self.isSubsetSum(arr, range_sum)
        
        # Possible subset sums from last row
        vector = [i for i in range(len(dp[-1])) if dp[-1][i] == True]
        
        min_diff = float('inf')
        for s in vector:
            min_diff = min(min_diff, abs(range_sum - 2*s))
            
        return min_diff
