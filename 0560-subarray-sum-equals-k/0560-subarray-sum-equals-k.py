class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [1,2,3,4,5,6,7] k = 7
        prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            temp = prefix_sum[i-1]
            prefix_sum.append(temp + nums[i])

        count = 0
        dic = {0: 1}  # Important: prefix sum 0 occurs once (handles subarrays starting at index 0)


        for i in range(len(prefix_sum)):
            target = prefix_sum[i] - k

            # If target exists, add its frequency to count
            if target in dic:
                count += dic[target]

            # Store/update frequency of current prefix_sum
            dic[prefix_sum[i]] = dic.get(prefix_sum[i], 0) + 1

        return count
            
                
        
        return count