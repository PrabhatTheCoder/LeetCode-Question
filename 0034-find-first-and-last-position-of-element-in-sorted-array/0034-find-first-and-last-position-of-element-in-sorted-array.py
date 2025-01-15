class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums)-1
        result1 = -1

        # first occurence
        while low<=high:
            mid = low + (high-low)//2

            if nums[mid] == target:
                result1 = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1


        low = 0
        high = len(nums)-1
        result2 = -1

        # last occurence
        while low<=high:
            mid = low + (high-low)//2

            if nums[mid] == target:
                result2 = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [result1,result2]

        
        