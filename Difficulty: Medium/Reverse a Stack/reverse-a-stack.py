#User function Template for python3

from typing import List

class Solution:
    
    def insert(self, St, temp):
        if len(St) == 0:
            St.append(temp)
            return
        
        val = St.pop()  # Store last element
        self.insert(St, temp)  # Insert temp at correct position
        St.append(val)  # Restore the popped element
        
        
    def reverse(self,St): 
        #code here
        
        if len(St) == 0:
            return

        temp = St.pop()  # Remove last element
        self.reverse(St)  # Recursively reverse the remaining stack
        self.insert(St, temp)  # Insert removed element at the correct position


#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
    print("~")
# } Driver Code Ends