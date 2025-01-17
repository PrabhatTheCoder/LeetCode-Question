class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            next_mid = (mid + 1) % n
            prev_mid = (mid + n - 1) % n
            
            if nums[mid] <= nums[next_mid] and nums[mid] <= nums[prev_mid]:
                minimum_element = mid
                break
            
            elif nums[mid] < nums[end]:  # Unsorted part is to the left of mid
                end = mid - 1
                
            else:  # Unsorted part is to the right of mid
                start = mid + 1

        if nums[n-1] < target:   # Value is in Unsorted Part
            end = mid - 1
            start = 0
        else:                     # Value is in sorted Part
            start = minimum_element
            end = n-1

        while start <= end:
            mid = start + (end-start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
            
