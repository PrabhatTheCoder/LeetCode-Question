import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        idx = len(nums) - k
        for _ in range(idx):
            heapq.heappop(nums)
        return heapq.heappop(nums)