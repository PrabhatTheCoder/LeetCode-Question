class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        if len(nums) == 1:
            return 0
        while low<=high:
            mid = low + (high-low)//2

            if mid > 0 and mid < len(nums)-1:
                if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid] < nums[mid+1]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    return mid+1
            elif mid == len(nums)-1:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    return mid-1

        return mid
        