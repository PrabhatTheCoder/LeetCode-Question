from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        ans = [0] * len(A)
        dic = {}
        
        for i in range(len(A)):
            ans[i] = ans[i-1] if i > 0 else 0   # carry forward previous count

            if A[i] in dic:
                ans[i] += 1
            else:
                dic[A[i]] = 1

            if B[i] in dic:
                ans[i] += 1
            else:
                dic[B[i]] = 1

        return ans
