class Solution(object):

    def rotatePoint(self,nums,i,j):
        
        while i<=j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

        return nums

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # rotate left numsay
        k = k % len(nums) # Handle cases where k is greater than the length of the array
        j = len(nums) - k - 1
        i = 0
        nums = self.rotatePoint(nums,i,j)

        # rotate right array
        i = j + 1
        j = len(nums) - 1
        nums = self.rotatePoint(nums,i,j)

        # rotate whole array
        i = 0
        j = len(nums) - 1
        nums = self.rotatePoint(nums,i,j)
        return nums
        

        