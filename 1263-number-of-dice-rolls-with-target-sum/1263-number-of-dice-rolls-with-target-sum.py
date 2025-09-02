class Solution:
    MOD = 10**9 + 7

    def solve(self, n, k, target):
        if target < 0:
            return 0
        if n == 0:
            return 1 if target == 0 else 0

        if self.t[n][target] != -1:
            return self.t[n][target]

        ways = 0
        for face in range(1, k+1):
            ways = (ways + self.solve(n-1, k, target-face)) % self.MOD

        self.t[n][target] = ways
        return self.t[n][target]

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # dp[n][target]
        self.t = [[-1]*(target+1) for _ in range(n+1)]
        return self.solve(n, k, target)
