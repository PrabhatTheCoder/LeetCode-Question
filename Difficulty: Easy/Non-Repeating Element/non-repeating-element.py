#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr): 
        # Complete the function
        dict = {}
        
        for i in range(len(arr)):
            if arr[i] in dict:
                dict[arr[i]] += 1
            else:
                dict[arr[i]] = 1
        for key in dict:
            if dict[key] == 1:
                return key
            
        return 0
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict

for _ in range(0, int(input())):
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr))

    print("~")

# } Driver Code Ends