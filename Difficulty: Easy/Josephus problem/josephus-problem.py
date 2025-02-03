#{ 
 # Driver Code Starts
import math



# } Driver Code Ends
#Complete this function

class Solution:
    
    def solve(self, nums, index, k):
        if len(nums) == 1:
            return nums[0]
        
        eliminate_idx = (index + k) % len(nums)
        del nums[eliminate_idx]
        
        return self.solve(nums, eliminate_idx, k)
        
        
    def josephus(self,n,k):
        #Your code here
        nums = []
        for i in range(n):
            nums.append(i + 1) 
        k -= 1
        return self.solve(nums, 0, k)
        

#{ 
 # Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        n=int(input())
        k=int(input())
        print(Solution().josephus(n,k))
        
        T-=1

        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends