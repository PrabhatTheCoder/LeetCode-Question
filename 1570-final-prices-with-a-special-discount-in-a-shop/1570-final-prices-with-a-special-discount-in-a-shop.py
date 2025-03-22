class Solution:
    def NearestSmallerToRight(self, nums):
        n = len(nums) - 1
        stack = []
        ans = []

        for i in range(n, -1, -1):
            if not stack:
                ans.append(0)

            elif stack[-1] <= nums[i]:
                ans.append(stack[-1])

            else:
                while stack and stack[-1] > nums[i]:
                    stack.pop()

                if not stack:
                    ans.append(0)
                else:
                    ans.append(stack[-1])

            stack.append(nums[i])

        ans.reverse()
        return ans


    def finalPrices(self, prices: List[int]) -> List[int]:
        val = self.NearestSmallerToRight(prices)
        res = []
        for i in range(len(prices)):
            res.append(prices[i] - val[i])
        return res