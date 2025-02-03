class Solution:

    def solve(self, nums, index, k):
        if len(nums) == 1:
            return nums[0]
        
        eliminate_idx = (index + k) % len(nums)
        del nums[eliminate_idx]
        
        return self.solve(nums, eliminate_idx, k)

    def findTheWinner(self, n: int, k: int) -> int:

        nums = []
        for i in range(n):
            nums.append(i + 1) 
        k -= 1
        return self.solve(nums, 0, k)
        