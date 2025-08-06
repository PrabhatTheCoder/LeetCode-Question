class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        # Build dictionary with value -> index
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]  # store indices in a list
            else:
                dic[nums[i]].append(i)

        # Check for pair
        for key in dic:
            find_ele = target - key
            
            # Case 1: Pair with different numbers
            if find_ele in dic and find_ele != key:
                return [dic[key][0], dic[find_ele][0]]
            
            # Case 2: Pair with same number (need at least two occurrences)
            if find_ele == key and len(dic[key]) > 1:
                return [dic[key][0], dic[key][1]]
