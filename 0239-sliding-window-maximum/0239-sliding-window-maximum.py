class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        j = 0
        ans = []
        queue = []
        while j < len(nums):
            while queue and nums[queue[-1]] < nums[j]:
                queue.pop()
            queue.append(j)

            if j - i + 1 == k:
                ans.append(nums[queue[0]])
                if queue[0] == i:
                    queue.pop(0)
                i += 1
            j += 1
        return ans