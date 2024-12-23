class Solution:
    def getThreeLargest(self, arr):
        third, second, first = -1, -1, -1
        
        for i in range(len(arr)):
            if arr[i] > first: 
                third = second
                second = first
                first = arr[i]
            elif arr[i] > second and arr[i] != first:
                third = second
                second = arr[i]
            elif arr[i] > third and arr[i] != second and arr[i] != first: 
                third = arr[i]
        newArr = []
        if first != -1:
            newArr.append(first)
        if second != -1:
            newArr.append(second)
        if third != -1:
            newArr.append(third)
        
        return newArr



#{ 
 # Driver Code Starts
import heapq
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))

        obj = Solution()
        ans = obj.getThreeLargest(arr)

        print(" ".join(map(str, ans)))
        print("~")

# } Driver Code Ends