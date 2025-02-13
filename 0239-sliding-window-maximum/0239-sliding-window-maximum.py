class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = []
        i = 0
        j = 0
        ans = []
        while j < len(nums):

            # Calculations
            while len(queue) > 0 and nums[j] > queue[-1] :
                queue.pop()
            queue.append(nums[j])
            # Check window size
            if j-i+1 == k:
                ans.append(queue[0])

                # Slide the window
                if queue[0] == nums[i]:
                    queue.pop(0)
                i += 1
            j += 1

        return ans

        