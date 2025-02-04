class Solution:

    def solve(self, nums, ans, result):
        if len(nums) == 0:
            result.append(ans[:])
            return
        for i in range(len(nums)):
            ans.append(nums[i])
            left = nums[:i]
            right = nums[i+1:]
            new_nums = left + right
            self.solve(new_nums,ans,result)
            ans.pop()
        return
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            ans = []
            ans.append(nums[i])
            left = nums[:i]
            right = nums[i+1:]
            new_nums = left + right
            self.solve(new_nums,ans,result)
        return result

        