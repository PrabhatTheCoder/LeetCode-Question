class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        # Sort the Array
        satisfaction.sort()

        suffix = 1
        suffix_sum = [None]*len(satisfaction)
        for i in range(len(satisfaction)-1,-1,-1):
            if i == len(satisfaction)-1:
                suffix_sum[i] = satisfaction[i]
                continue
            suffix_sum[i] = satisfaction[i] + suffix_sum[i+1]
        
        # Find the Pivot index
        idx = -1
        for i in range(len(suffix_sum)):
            if suffix_sum[i] >= 0:
                idx = i
                break

        if idx == -1:
            return 0
            
        # Find the Max- like time Coefficient
        maxSum = 0
        x = 1
        for i in range(idx,len(satisfaction)):
            maxSum += satisfaction[i] * x
            x += 1
        return maxSum