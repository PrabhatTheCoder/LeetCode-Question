from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_max = [0] * n
        suffix_max = [0] * n

        # prefix_max[i] = max(nums[0..i])
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])

        # suffix_max[i] = max(nums[i..n-1])
        suffix_max[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], nums[i])

        ans = 0
        for j in range(1, n-1):
            val = (prefix_max[j-1] - nums[j]) * suffix_max[j+1]
            ans = max(ans, val)

        return ans
