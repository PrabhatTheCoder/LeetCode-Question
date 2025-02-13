class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = {}
       
        for i in range(len(p)):
            if p[i] not in d:
                d[p[i]] = 1
            else:
                d[p[i]] += 1
                
        count = len(d)
        
        
        j = 0
        i = 0
        ans = []
        
        while j < len(s):
            
            if s[j] in d:
                
                d[s[j]] -= 1
                
                if d[s[j]] == 0:
                    count -= 1
            
           
            if (j - i + 1) == len(p):
                
                if count == 0:
                    ans.append(i)
                
                
                if s[i] in d:
                    
                    if d[s[i]] == 0:
                        count += 1
                    d[s[i]] += 1
                i += 1
            
           
            j += 1
            
        return ans
        