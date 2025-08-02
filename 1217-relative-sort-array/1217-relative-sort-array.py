class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        for i in range(len(arr1)):
            if arr1[i] not in dic:
                dic[arr1[i]] = 1
            else:
                dic[arr1[i]] += 1

        res = []
        for val in arr2:
            ans = [val] * dic[val]
            res.extend(ans)
            dic[val] = 0
        
        asc = []
        for key in dic:
            if dic[key] > 0:
                ans = [key] * dic[key]
                asc.extend(ans)
                dic[val] = 0
        asc.sort()
        res.extend(asc)

        return res

        
        