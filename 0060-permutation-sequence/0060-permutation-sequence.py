class Solution:

    def solve(self, nums, ans, k):

        if len(nums) == 1:
            ans += str(nums[0])
            return ans

        # find fact(len(nums)-1)
        fact = 1
        for i in range(1,len(nums)):
            fact *= i

        idx = k // fact
        if k%fact == 0:
            idx -= 1
            k = fact
        else:
            k = k%fact

        ans += str(nums[idx])
        left = nums[:idx]
        right = nums[idx+1:]
        print(left+right, ans, k)
        return self.solve(left+right, ans, k)

    def getPermutation(self, n: int, k: int) -> str:
        nums = ""
        for i in range(1,n+1):
            nums += str(i)
        
        ans = ""
        return self.solve(nums, ans , k)