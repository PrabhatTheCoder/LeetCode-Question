import heapq

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Build frequency map
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Step 2: Min-heap: (frequency, -value) for value-desc tie-breaking
        min_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, -num))

        # Step 3: Pop and build result
        res = []
        while min_heap:
            freq, neg_num = heapq.heappop(min_heap)
            num = -neg_num
            res.extend([num] * freq)

        return res
