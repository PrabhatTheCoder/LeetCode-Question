import heapq

class Solution:
    def nearlySorted(self, arr, k):
        min_heap = []
        idx = 0
        for i in range(len(arr)):
            heapq.heappush(min_heap, arr[i])
            
            
            if len(min_heap) > k:
                temp = heapq.heappop(min_heap)
                arr[idx] = temp
                idx += 1
                
        while min_heap:
            temp = heapq.heappop(min_heap)
            arr[idx] = temp
            idx += 1
            
        return arr