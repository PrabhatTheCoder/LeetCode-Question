#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
		
		low = 0
        high = len(arr)-1
        
        while low<=high:
            
            mid = low + (high-low)//2
            
            # Handle single-element list or peak at the edges
            if len(arr) == 1 or mid == 0 and arr[mid] > arr[mid + 1]:
                return arr[mid]
            elif mid == len(arr) - 1 and arr[mid] > arr[mid - 1]:
                return arr[mid]
            
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return arr[mid]
            elif arr[mid] < arr[mid+1]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
                    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends