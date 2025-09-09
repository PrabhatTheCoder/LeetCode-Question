class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
   
        n = len(coins)
        dp = [[0 for j in range(amount + 1)] for i in range(n + 1)]

        # Base case: amount = 0 => 1 way (take nothing)
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]  # exclude coin
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]  # exclude + include (unbounded)

        return dp[n][amount]
