class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for val in stones:
            heapq.heappush(max_heap, -val)
        
        while len(max_heap) >= 2:
            print(max_heap)
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            x = min(x,y)
            y = max(x,y)

            if x == y:
                continue

            if x != y:
                y = y-x
                heapq.heappush(max_heap, -y)

        return abs(heapq.heappop(max_heap)) if len(max_heap) > 0 else 0


        