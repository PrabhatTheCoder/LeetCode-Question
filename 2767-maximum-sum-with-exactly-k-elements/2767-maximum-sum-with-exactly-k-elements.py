class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum_val = 0
        
        for i in range(k):
            sum_val += nums[-1]
            nums[-1] = nums[-1] + 1

        return sum_val
        
