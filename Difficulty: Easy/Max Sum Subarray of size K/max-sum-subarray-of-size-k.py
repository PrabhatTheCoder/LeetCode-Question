#User function Template for python3
class Solution:
    def maximumSumSubarray(self, arr, k):
        maxSum = float('-inf')  # Initialize to negative infinity to handle negative values
        val = 0  # Holds the sum of the current window
            
        i = 0
        j = 0

        while j < len(arr):
            val += arr[j]  # Add current element to window sum
            
            if (j - i + 1) == k:  # When window size reaches 'k'
                maxSum = max(maxSum, val)  # Update maxSum
                val -= arr[i]  # Remove leftmost element of the window
                i += 1  # Slide the window forward
            
            j += 1  # Expand the window
            
        return maxSum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.maximumSumSubarray(arr, k)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends