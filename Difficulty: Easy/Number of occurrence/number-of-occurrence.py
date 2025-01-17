class Solution:
    def countFreq(self, arr, target):
        #code here
        
        low = 0
        high = len(arr)-1
        result1 = -1

        # first occurence
        while low<=high:
            mid = low + (high-low)//2

            if arr[mid] == target:
                result1 = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        low = 0
        high = len(arr)-1
        result2 = -1

        # last occurence
        while low<=high:
            mid = low + (high-low)//2

            if arr[mid] == target:
                result2 = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        if result1 != -1 and result2 != -1:
            return result2-result1+1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends