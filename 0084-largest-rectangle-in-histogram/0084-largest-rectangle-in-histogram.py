class Solution:

    def smaller_to_right(self, nums):
        stack = []
        ans = [len(nums)] * len(nums) 
        for j in range(len(nums)-1, -1, -1):
            while stack and stack[-1][0] >= nums[j]:
                stack.pop()

            if stack:
                ans[j] = stack[-1][1]  
            else:
                ans[j] = len(nums)  

            stack.append((nums[j], j))

        return ans

    def smaller_to_left(self, nums):
        ans = [-1] * len(nums)   
        stack = []

        for j in range(len(nums)):
            while stack and stack[-1][0] >= nums[j]:
                stack.pop()
            
            if stack:
                ans[j] = stack[-1][1]  
            else:
                ans[j] = -1            

            stack.append((nums[j], j))

        return ans
            
    def largestRectangleArea(self, heights: List[int]) -> int:
        right = self.smaller_to_right(heights)
        left = self.smaller_to_left(heights)

        max_area = 0

        for i in range(len(heights)):
            width = right[i] - left[i] - 1  
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area
