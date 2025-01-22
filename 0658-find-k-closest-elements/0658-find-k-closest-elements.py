from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr) - 1

        # Binary search to find the closest element or potential insertion point
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid

        # Initialize two pointers for the sliding window
        left = low - 1
        right = low

        # Expand the window to include `k` closest elements
        while k > 0:
            if left >= 0 and (right >= len(arr) or abs(arr[left] - x) <= abs(arr[right] - x)):
                left -= 1
            else:
                right += 1
            k -= 1

        # Return the sorted subarray
        return arr[left + 1:right]
