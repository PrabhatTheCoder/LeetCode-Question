class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = 1
            else:
                dic[arr[i]] += 1

        seen = set()
        for key in dic:
            if dic[key] in seen:
                return False
            seen.add(dic[key])

        return True
