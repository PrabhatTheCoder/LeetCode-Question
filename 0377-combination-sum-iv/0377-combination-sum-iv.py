class Solution:

    def solve(self, nums, target):
        if target == 0:
            return 1

        if target < 0:
            return 0

        if self.dp[target] != -1:
            return self.dp[target]

        ways = 0
        for num in nums:      
            ways += self.solve(nums, target - num)

        self.dp[target] = ways
        return ways

    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.dp = [-1] * (target+1)
        return self.solve(nums, target)
        
        