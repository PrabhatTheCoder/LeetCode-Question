import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(len(points)):
            val = (points[i][0])**2 + (points[i][1])**2
            heapq.heappush(max_heap, [-val, (points[i][0], points[i][1])])

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        for val in max_heap:
            res.append(val[1])

        return res
        



        