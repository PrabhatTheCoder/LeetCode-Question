class Solution:     

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # DP array
        t = [0] * (n+1)
        t[0] = 0
        t[1] = nums[0]

        for i in range(2, n+1):
            print(t)
            steal = nums[i-1] + t[i-2]   # include current house
            skip = t[i-1]                # skip current house
            t[i] = max(steal, skip)

        return t[n]