''' 
Given two sorted arrays A and B, generate all possible arrays such that the first element is taken 
from A then from B then from A, and so on in increasing order till the arrays are exhausted. The 
generated arrays should end with an element from B.
 A = {10, 15, 25}
 B = {1, 5, 20, 30}
 Output: {10 20}, {10 20 25 30}, {10 30}, {15 20}, {15 20 25 30}, {15 30}, 
{25 30}
'''


class Solution:
    
    def solve(self, numsA, numsB, ans, flag):
        if flag: 
            nums = numsA
        else:   
            nums = numsB

        for i in range(len(nums)):
            if not ans or ans[-1] < nums[i]:
                ans.append(nums[i])
                
                if not flag:
                    print(ans)
                
                self.solve(numsA, numsB, ans, not flag)
                ans.pop()
    
    def printArr(self,numsA,numsB):
        for i in range(len(numsA)):
            ans = [numsA[i]] 
            self.solve(numsA, numsB, ans, False) 
            
            
# Test the code
A = [10, 15, 25]
B = [1, 5, 20, 30]

sol = Solution()
sol.printArr(A, B)
