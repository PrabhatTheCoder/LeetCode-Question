#User function Template for python3
class Solution:
    
    def solve(self, val, zero, ones, n, result):
        if len(val) == n:
            result.append(val)
            return
        if ones  <=  n:
            val1 = val + "1"
            self.solve(val1, zero, ones+1, n, result)
        if ones > zero:
            val2 = val + "0"
            self.solve(val2, zero+1, ones, n, result)
            
	def NBitBinary(self, n):
		# code here
		zero = n
		ones = n
		result = []
		self.solve("",0,0,n, result)
		return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        answer = ob.NBitBinary(n)
        for value in answer:
            print(value, end=" ")
        print()
        print("~")

# } Driver Code Ends