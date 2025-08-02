class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            print(s[i])
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in dic:
                return False
            else:
                dic[t[i]] -= 1
                if dic[t[i]] < 0:
                    return False

        for key in dic:
            if dic[key] != 0:
                return False

        return True