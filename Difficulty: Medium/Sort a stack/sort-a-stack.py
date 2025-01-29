class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    
    
    def insert(self, s, temp):
        if len(s) == 0 or s[-1] <= temp:
            s.append(temp)  # Corrected push() to append()
            return
        
        val = s.pop()  # Remove last element
        self.insert(s, temp)  # Insert temp in sorted order
        s.append(val)  # Restore popped element
        
        
    def Sorted(self, s):
        # Code here
        
        if len(s) == 1:
            return
        
        temp = s.pop()  # Remove last element
        self.Sorted(s)  # Recursively sort the remaining say
        
        
        self.insert(s, temp)  # Insert removed element at correct position




#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


        print("~")
# } Driver Code Ends