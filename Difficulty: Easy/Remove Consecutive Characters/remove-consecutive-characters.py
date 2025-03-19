#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, s):
        # code here
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                continue 
            else:
                stack.append(char)
        return ''.join(stack)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

        print("~")
# } Driver Code Ends