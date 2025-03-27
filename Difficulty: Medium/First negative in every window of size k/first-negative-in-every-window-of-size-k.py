#User function Template for python3

class Solution:
    def firstNegInt(self, arr, k): 
         # code here 
        i = 0
        j = 0
        res = []
        queue = []
        while j < len(arr):
            
            if arr[j] < 0:
                queue.append(arr[j])
                
            while j-i+1 == k:
                if queue and queue[0] == arr[i]:
                    res.append(queue.pop(0))
                elif queue and queue[0] != arr[i]:
                    res.append(queue[0])
                else:
                    res.append(0)
                i += 1
            j += 1
        return res



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
        ans = ob.firstNegInt(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends