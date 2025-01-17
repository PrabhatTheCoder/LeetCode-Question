#User function Template for python3
class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        start = 0
        end = n - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            next_mid = (mid + 1) % n
            prev_mid = (mid + n - 1) % n
            
            if arr[mid] <= arr[next_mid] and arr[mid] <= arr[prev_mid]:
                return mid
            
            elif arr[mid] < arr[end]:  # Unsorted part is to the left of mid
                end = mid - 1
                
            else:  # Unsorted part is to the right of mid
                start = mid + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.findKRotation(arr)
        print(res)
        print("~")
# } Driver Code Ends