from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.dic2 = {}

        # Build initial frequency map for nums2
        for num in nums2:
            self.dic2[num] = self.dic2.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        self.nums2[index] = new_val

        # Update frequency map
        self.dic2[old_val] -= 1
        # if self.dic2[old_val] == 0:
        #     del self.dic2[old_val]
        self.dic2[new_val] = self.dic2.get(new_val, 0) + 1

    def count(self, tot: int) -> int:
        count_pairs = 0
        for num1 in self.nums1:
            complement = tot - num1
            count_pairs += self.dic2.get(complement, 0)
        return count_pairs


                

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)