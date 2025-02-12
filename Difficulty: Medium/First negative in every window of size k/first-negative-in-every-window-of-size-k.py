#User function Template for python3

class Solution:
    def FirstNegativeInteger(self, arr, k): 
        ans = []
        deque = []
        i = 0
        j = 0
        
        while j < len(arr):
            # Collect negative numbers in the window
            if arr[j] < 0:
                deque.append(arr[j])
            
            # Check if the window size is reached
            if (j - i + 1) == k:
                # Add the first negative number of the window to the answer
                if deque:
                    ans.append(deque[0])
                else:
                    ans.append(0)  # No negative number in this window
                
                # Slide the window
                if arr[i] < 0:
                    deque.pop(0)
                i += 1
            
            j += 1
        
        return ans





#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())

        if k <= 0 or k > len(arr):
            tc -= 1
            continue

        ob = Solution()
        ans = ob.FirstNegativeInteger(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends