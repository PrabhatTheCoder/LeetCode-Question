#User function Template for python3

class Solution:
    
    def solve(self, op, inp, result):
        if len(inp) == 0:
            if op:  
                result.append(op) 
            return
        
        # Recursive calls
        # 1. Exclude the current character
        self.solve(op, inp[1:], result)

        # 2. Include the current character
        self.solve(op + inp[0], inp[1:], result)
        
    def AllPossibleStrings(self, s):
        result = [] 
        self.solve("", s, result)
        result.sort() 
        return result 

		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ob = Solution()
        ans = ob.AllPossibleStrings(s)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends