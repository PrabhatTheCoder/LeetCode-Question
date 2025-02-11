class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        conver = [0]*n

        val = 0
        for i in range(n):
            if nums[i] >= nums[val]:
                val = i
            conver[i] = nums[i] + nums[val]
        
        ans = [0]*n
        ans[0] = conver[0]
        for i in range(1,n):
            ans[i] = ans[i-1] + conver[i]
        return ans 

