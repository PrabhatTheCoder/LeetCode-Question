class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = {}  
        
        for c in s:
            if c not in cnt:
                cnt[c] = 1
            else:
                cnt[c] += 1
                
        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
        
        return -1