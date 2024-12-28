class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i = 0
        j = len(nums)-1
        result = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1

            if i>0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while nums[left] == nums[left-1] and left < right:
                        left += 1

                    while nums[right] == nums[right+1] and left < right:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
            



