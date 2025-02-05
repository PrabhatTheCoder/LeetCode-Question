class Solution:
    def decToBinary(self, n):
        # code here
        
        binary=''
        r=0
        while n:
            r=n%2
            n=n//2
            binary=str(r)+binary
        return int(binary)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    solution = Solution()

    for _ in range(t):
        n = int(input())
        print(solution.decToBinary(n))
        print("~")

# } Driver Code Ends