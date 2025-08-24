class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n 

        subArray = nums[len(nums)-k:]
        move_idx = len(nums)-1-k

        right = len(nums)-1
        while move_idx >= 0:
            nums[right] = nums[move_idx]
            right -= 1
            move_idx -= 1

        for i in range(len(subArray)):
            nums[i] = subArray[i]

        return nums

        