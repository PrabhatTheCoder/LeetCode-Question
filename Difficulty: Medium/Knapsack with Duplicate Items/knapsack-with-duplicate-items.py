#User function Template for python3

class Solution:
    
    def solve(self, W, val, wt, n):
        # Base Case
        if n == 0 or W == 0:
            return 0

        # Already computed
        if self.dp[n][W] != -1:
            return self.dp[n][W]

        # If weight of nth item <= capacity
        if wt[n-1] <= W:
            self.dp[n][W] = max(
                val[n-1] + self.solve(W - wt[n-1], val, wt, n),
                self.solve(W, val, wt, n-1)
            )
        else:
            # Can't take it
            self.dp[n][W] = self.solve(W, val, wt, n-1)
        
        return self.dp[n][W]
        
    def knapSack(self, val, wt, capacity):
        n = len(wt)
        self.dp = [[-1] * (W+1) for _ in range(n+1)]  # DP[n][W]
        return self.solve(capacity, val, wt, n)
