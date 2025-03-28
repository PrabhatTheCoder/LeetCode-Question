#User function Template for python3
class Solution:
    
    def solve(self, arr, ans, result):
        
        if len(arr) == 0:
            return
        
        for i in range(len(arr)):
            ans.append(arr[i])
            result.append(ans[:])
            
            
    def getSubArrays(self, arr):
        #code here
        result = []
        for i in range(len(arr)):
            ans = []
            ans.append(arr[i])
            result.append(ans[:])
            right = arr[i+1:]
            self.solve(right,ans,result)
            
        return result
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())  # Read the number of test cases
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.getSubArrays(arr)

        # Print the result in the required format
        print("[", end="")
        for i, subarray in enumerate(result):
            print("[", end="")
            for j, num in enumerate(subarray):
                if j != len(subarray) - 1:
                    print(num, end=",")
                else:
                    print(num, end="")
            print("]", end="")
            if i != len(result) - 1:
                print(", ", end="")
        print("]")
        print("~")

# } Driver Code Ends