class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                res.append(nums[i])
                i += 2
            else:
                i += 1
        return res
        