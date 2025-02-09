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
            for j in range(len(nums_prefix_sum)):
                if nums_prefix_sum[j] <= queries[i]:
                    answer[i] = j+1 
        return answer
        