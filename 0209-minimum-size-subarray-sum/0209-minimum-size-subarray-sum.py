class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        ans = float('inf')

        i = 0
        j = 0
        while j < len(nums):

            total += nums[j]
            while total >= target:
                ans = min(ans, j - i + 1)
                total -= nums[i]
                i += 1
            j += 1

        return ans if ans != float('inf') else 0
        