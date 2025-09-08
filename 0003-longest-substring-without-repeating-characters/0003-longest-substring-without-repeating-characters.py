class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        i, j = 0, 0
        total = 0

        while j < len(s):
            if s[j] in dic and dic[s[j]] >= i:
                # move i just after the duplicate
                i = dic[s[j]] + 1

            dic[s[j]] = j   # update last seen index
            curr = j - i + 1
            total = curr if curr > total else total
            j += 1

        return total
