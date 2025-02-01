class Solution:
    def solve(self, op, inp, result):
        # ✅ Base Case: If the input is exhausted, add the output to the result
        if len(inp) == 0:
            result.append(op)
            return
        
        # ✅ Recursive Calls:
        # 1️⃣ Include space before adding the next character
        self.solve(op + " " + inp[0], inp[1:], result)
        
        # 2️⃣ Exclude space, add the character directly
        self.solve(op + inp[0], inp[1:], result)

    def permutation(self, s):
        result = []
        
        # ✅ Edge Case: Handle empty input
        if not s:
            return "()"
        
        # Start recursion with the first character
        self.solve(s[0], s[1:], result)
        
        # ✅ Sort the result lexicographically
        result.sort()

        return result


# # ✅ Test Cases
# sol = Solution()

# # Test Case 1
# s1 = "ABC"
# print(sol.permutation(s1))  # Expected: (A B C)(A BC)(AB C)(ABC)

# # Test Case 2
# s2 = "BBR"
# print(sol.permutation(s2))  # Expected: (B B R)(B BR)(BB R)(BBR)

        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        S = input()
        ans = ob.permutation(S)
        write = ""
        for i in ans:
            write += "(" + i + ")"
        print(write)

        print("~")
# } Driver Code Ends
