class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        char_count = {}
        
        for i in range(len(nums)):
            if nums[i] in char_count:
                char_count[nums[i]] += 1
            else:
                char_count[nums[i]] = 1

        for key in char_count:
            if char_count[key] == 1:
                return key
            
        return 0
        