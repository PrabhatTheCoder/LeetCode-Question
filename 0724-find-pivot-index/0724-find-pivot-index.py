class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        prefixSum = [0]*n
        prefixSum[0] = nums[0]
        for i in range(1,n):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        
        suffixSum = [0]*n
        suffixSum[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suffixSum[i] = suffixSum[i+1] + nums[i]
        
        for i in range(n):
            if suffixSum[i] ==  prefixSum[i]:
                return i
        return -1
            
        