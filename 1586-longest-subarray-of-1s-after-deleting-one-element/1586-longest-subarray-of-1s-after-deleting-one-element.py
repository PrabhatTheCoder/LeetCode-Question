class Solution:

    def longestSubarray(self, nums):
        
        maxVal = 0
        zerosCount = 0
        i = 0
        j = 0
        
        while j < len(nums):
            if nums[j] == 0:
                zerosCount += 1
            
            while zerosCount > 1:
                if nums[i] == 0:
                    zerosCount -= 1
                i += 1
            
            maxVal = max(maxVal, j - i)
            j += 1

        return maxVal
