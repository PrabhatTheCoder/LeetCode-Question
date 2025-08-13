class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []

        for val in arr:
            dist = abs(val - x)
            heapq.heappush(max_heap, (-dist, -val)) # Max Heap

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        result = [-val for (_, val) in max_heap]
        result.sort()
        return result
        