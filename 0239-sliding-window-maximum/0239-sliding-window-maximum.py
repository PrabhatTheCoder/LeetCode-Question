class Solution:

    def NextGreaterIndex(self, nums):
        ans = []
        stack = []
        n = len(nums)
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:  # Corrected comparison
                stack.pop()
            if not stack:
                ans.append(n)
            else:
                ans.append(stack[-1])
            stack.append(i)
        ans.reverse()
        return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        nxtIdx = self.NextGreaterIndex(nums)
        ans = []
        i = 0
        n = len(nums)
        j = 0
        for i in range(n-k+1):
            if j < i:
                j = i

            mx = nums[j]

            while j < i + k:
                mx = nums[j]
                if nxtIdx[j] >= i+k:
                    break
                j = nxtIdx[j]
            ans.append(mx)

        return ans
        