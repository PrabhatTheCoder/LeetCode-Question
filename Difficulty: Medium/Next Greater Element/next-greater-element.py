# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        stack = []
        ans = []
        n = len(arr)
        for i in range(n-1, -1, -1):
            if len(stack) == 0:
                ans.append(-1)
                
            elif stack and arr[i] < stack[-1]:
                ans.append(stack[-1])
                
            elif stack and arr[i] >= stack[-1]:
            
                while stack and arr[i] >= stack[-1]:
                    stack.pop()
                    
                if not stack:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
                    
            stack.append(arr[i])
            
        ans.reverse()
        return ans



#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends