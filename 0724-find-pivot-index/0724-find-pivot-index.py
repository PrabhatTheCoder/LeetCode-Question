class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left_sum = 0
        sum = 0
        right_sum = 0

        for i in range(len(nums)):
            sum += nums[i]   

        for j in range(len(nums)):
            
            right_sum = sum - left_sum - nums[j]

            if left_sum == right_sum:
                return j

            left_sum += nums[j]

        return -1