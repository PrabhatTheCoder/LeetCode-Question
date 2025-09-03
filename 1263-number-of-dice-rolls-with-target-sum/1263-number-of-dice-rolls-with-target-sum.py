MOD = 10**9 + 7

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # dp[i][j] = number of ways to get sum j with i dice
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # 1 way to get sum 0 with 0 dice

        for i in range(1, n + 1):  # number of dice
            for j in range(1, target + 1):  # target sum
            
                for face in range(1, k + 1):  # dice face values
                    if j >= face:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - face]) % MOD

        return dp[n][target]
