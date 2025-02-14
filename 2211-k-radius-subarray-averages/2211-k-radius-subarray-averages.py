class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1]*len(nums)

        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        i = 0
        j = 2 * k
        mid = k

        while j < len(nums):
            if i-1 < 0:
                total = prefix_sum[j]
            else:
                total = prefix_sum[j] - prefix_sum[i - 1]

            divisor = j-i+1
            ans[mid] = total//divisor

            mid += 1
            i += 1
            j += 1

        return ans

        