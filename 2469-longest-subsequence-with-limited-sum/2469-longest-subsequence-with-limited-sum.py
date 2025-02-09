class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        nums_prefix_sum = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                nums_prefix_sum[i] = nums[i]
            else:
                nums_prefix_sum[i] = nums_prefix_sum[i-1] + nums[i]
        
        answer = [0]*len(queries)
        for i in range(len(queries)):
            val = self.BinarySearch(nums_prefix_sum, queries[i]) 
            if val == -1:
                answer[i] = 0
            else:
               answer[i] = val + 1
        return answer
        
    def BinarySearch(self, nums, target):
        low = 0
        high = len(nums)-1
        maxVal = -1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] <= target:
                maxVal = mid
                low = mid + 1
            else:
                high = mid - 1
        return maxVal