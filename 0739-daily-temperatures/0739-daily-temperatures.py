class Solution:

    def next_greater_ele(self, nums):
        stack = []
        ans = [0]* len(nums)
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1][1] - i
            else:
                ans[i] = 0

            stack.append((nums[i],i))
        return ans

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        val = self.next_greater_ele(temperatures)
        return val
