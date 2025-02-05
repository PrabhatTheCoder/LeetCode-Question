class Solution:
    def canSplit(self, arr):
        #code 
        ans = []
        for i in range(len(arr)):
            if len(ans) == 0:
                ans.append(arr[i])
                continue
            val = ans[i-1] + arr[i]
            ans.append(val)
            
        for i in range(len(ans)):
            left = ans[i]
            right = ans[len(ans)-1] - left
            if left == right:
                return True
        return False
        
        

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends