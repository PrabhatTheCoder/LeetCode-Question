class Solution:

    def solve(self,a,b):
        if a == 0:
            return b
        return self.solve(b%a,a)

    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return self.solve(nums[0],nums[-1])
        