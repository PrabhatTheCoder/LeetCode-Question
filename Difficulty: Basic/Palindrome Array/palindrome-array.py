
from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        # code here
        i = 0
        j = len(arr)-1
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.isPerfect(arr)

        if res:
            print("true")
        else:
            print('false')
        print("~")
# } Driver Code Ends