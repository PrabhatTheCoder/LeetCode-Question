#User function Template for python3
class Solution:

	
	def search(self,pat, txt):
	    d = {}
       
        for i in range(len(pat)):
            if pat[i] not in d:
                d[pat[i]] = 1
            else:
                d[pat[i]] += 1
                
        count = len(d)
        
        
        j = 0
        i = 0
        ans = 0
        
        while j < len(txt):
            
            if txt[j] in d:
                
                d[txt[j]] -= 1
                
                if d[txt[j]] == 0:
                    count -= 1
            
           
            if (j - i + 1) == len(pat):
                
                if count == 0:
                    ans += 1
                
                
                if txt[i] in d:
                    
                    if d[txt[i]] == 0:
                        count += 1
                    d[txt[i]] += 1
                i += 1
            
           
            j += 1
            
        return ans

	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
        print("~")
# } Driver Code Ends