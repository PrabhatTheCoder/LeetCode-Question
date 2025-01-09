class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        res = ""
        i = 0
        while i <= len(strs[0])-1:
            print(i)        
            if strs[0][i] == strs[-1][i]:
                res += strs[0][i]
                i += 1
            else:
                break
        return res
        