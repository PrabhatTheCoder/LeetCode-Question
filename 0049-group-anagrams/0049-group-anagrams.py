class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(len(strs)):
            temp = ''.join(sorted(strs[i]))
            if temp not in dic:
                dic[temp] = [strs[i]]
            else:
                dic[temp].append(strs[i])
                
        res = []
        for key in dic:
            res.append(dic[key])
        return res
        