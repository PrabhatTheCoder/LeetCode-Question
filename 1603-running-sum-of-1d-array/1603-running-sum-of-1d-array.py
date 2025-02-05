class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if len(ans) == 0:
                ans.append(nums[0])
                continue
            val = ans[i-1] + nums[i]
            ans.append(val)
        return ans