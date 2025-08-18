class Solution:
   def minCost(self, arr):
       
        min_heap = []
        for val in arr:
            heapq.heappush(min_heap, val)
            
        total_cost = 0
        while len(min_heap) >= 2:
            
            val1 = heapq.heappop(min_heap)
            val2 = heapq.heappop(min_heap)
            
            temp = val1 + val2
            total_cost += temp
            heapq.heappush(min_heap, temp)
            
        return total_cost
           
          
        
    # code here