class Solution:

    def longestSubarray(self, nums):
        
        maxVal = 0
        zerosCount = 0
        i = 0
        j = 0
        last_zero_idx = -1
        while j < len(nums):
            if nums[j] == 0:
                i = last_zero_idx + 1
                last_zero_idx = j

            maxVal = max(maxVal, j - i)
            j += 1

        return maxVal
