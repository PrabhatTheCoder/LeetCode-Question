class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        set_list = set()
        for j in range(len(nums)):
            if nums[j] in set_list:
                return True
            
            set_list.add(nums[j])
            
            # Maintain the window size of at most k
            if len(set_list) > k:
                set_list.remove(nums[j - k])
        
        return False
        