class Solution:

    def helper(self, right, down, m, n, dp):
        if right == n-1 and down == m-1:
            return 1

        if right >= n or down >= m:
            return 0

        if dp[right][down] != -1:
            return dp[right][down]
        
        right_paths = self.helper(right + 1, down, m, n, dp)
        down_paths = self.helper(right, down + 1, m, n, dp)
        dp[right][down] = right_paths + down_paths
        return dp[right][down]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        return self.helper(0, 0, m, n, dp)