#{ 
 # Driver Code Starts

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findTarget(self, arr, target):
        n = len(arr)
        low = 0
        high = n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # Check if the mid element is the target
            if arr[mid] == target:
                return mid
            
            # Check the adjacent positions
            if mid > low and arr[mid - 1] == target:
                return mid - 1
            if mid < high and arr[mid + 1] == target:
                return mid + 1
            
            # Adjust the search range
            if arr[mid] < target:
                low = mid + 2  # Skip mid and mid + 1
            else:
                high = mid - 2  # Skip mid and mid - 1
        
        return -1

        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())  # Number of test cases

    for _ in range(t):
        arr = list(map(int, input().strip().split()))  # Read the array
        target = int(input().strip())  # Read the target

        sln = Solution()
        ans = sln.findTarget(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends