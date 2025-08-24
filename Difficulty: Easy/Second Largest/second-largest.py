class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1  # Not enough elements

        first_ele = float('-inf')
        sec_ele = float('-inf')

        for num in arr:
            if num > first_ele:
                sec_ele = first_ele
                first_ele = num
            elif first_ele > num > sec_ele:
                sec_ele = num

        return sec_ele if sec_ele != float('-inf') else -1
