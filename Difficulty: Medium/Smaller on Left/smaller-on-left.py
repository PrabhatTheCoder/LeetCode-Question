# User function Template for Python3

class Solution:
    def leftSmaller(self, n, arr):
        # code here
        stack = []
        ans = []
        n = len(arr)
        for i in range(n):
            if len(stack) == 0:
                ans.append(-1)
                
            elif stack and arr[i] > stack[-1]:
                ans.append(stack[-1])
                
            elif stack and arr[i] <= stack[-1]:
            
                while stack and arr[i] <= stack[-1]:
                    stack.pop()
                    
                if not stack:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
                    
            stack.append(arr[i])
            
        return ans


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
        print("~")
# } Driver Code Ends