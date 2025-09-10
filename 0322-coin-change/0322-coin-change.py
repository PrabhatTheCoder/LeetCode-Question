class Solution:
    def coinChange(self, coins, amount):
        arraySize = len(coins)
        dp = [[0 if j == 0 else float('inf') for j in range(amount + 1)] for i in range(arraySize + 1)]

        for i in range(1, arraySize + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])

        res = dp[arraySize][amount]
        return -1 if res == float('inf') else res
