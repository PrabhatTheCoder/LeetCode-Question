class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = 1
            else:
                dic[arr[i]] += 1
        dic2 = {}
        for key in dic:
            if dic[key] not in dic2:
                dic2[dic[key]] = 1
            else:
                return False
        return True