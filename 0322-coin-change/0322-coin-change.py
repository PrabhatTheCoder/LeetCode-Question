class Solution:
    def solve(self, amount, memo):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')

        if memo[amount] != -1:
            return memo[amount]

        res = float('inf')
        for coin in self.coins:
            res = min(res, self.solve(amount - coin, memo))

        memo[amount] = 1 + res
        return memo[amount]

    def coinChange(self, coins, amount):
        self.coins = coins
        memo = [-1] * (amount + 1)   # array for memoization
        ans = self.solve(amount, memo)
        return -1 if ans == float('inf') else ans
