class Solution:

    def MaxAtLeft(self, nums):
        res = [0] * len(nums)
        res[0] = nums[0]
        
        for i in range(1, len(nums)):
            res[i] = max(res[i-1], nums[i-1])  
        return res

    def MaxAtRight(self, nums):
        res = [0] * len(nums)
        res[-1] = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            res[i] = max(res[i+1], nums[i+1])  # Fix: Compare with the next element, not current

        return res

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = self.MaxAtLeft(height)
        right = self.MaxAtRight(height)
        water = [0] * len(height)

        for i in range(len(height)):
            water[i] = max(0, min(left[i], right[i]) - height[i])  
        
        return sum(water)
