'''
Print all increasing sequences of length k from first n natural numbers
'''



class Solution:
    
    def solve(self,nums,k,ans,result):
        if len(ans) == k:
            result.append(ans[:])
        
        for i in range(len(nums)):
            ans.append(nums[i])
            right = nums[i+1:]
            self.solve(right,k,ans,result)
            ans.pop()
        
    
    def printArr(self,k,n):
        nums = []
        for i in range(1,n+1):
            nums.append(i)

        result = []
        for i in range(len(nums)):
            ans = []
            ans.append(nums[i])
            right = nums[i+1:]
            self.solve(right,k,ans,result)
            
        return result
            
            
            
# Test the code
k = 3
n = 5

sol = Solution()
val = sol.printArr(k,n)
print(val)
