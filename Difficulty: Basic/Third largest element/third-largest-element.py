class Solution:
    def thirdLargest(self,arr):
        third, second, first = -1, -1, -1
        
        for i in range(len(arr)):
            if arr[i] > first: 
                third = second
                second = first
                first = arr[i]
            elif arr[i] > second:
                third = second
                second = arr[i]
            elif arr[i] > third: 
                third = arr[i]
        
        return third


#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr))
        print("~")

# } Driver Code Ends