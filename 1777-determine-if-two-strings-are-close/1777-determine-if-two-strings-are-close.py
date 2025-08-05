class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0 for i in range(26)]
        freq2 = [0 for i in range(26)]

        if len(word1) != len(word2):
            return False

        for i in range(len(word1)):
            ch1 = ord(word1[i]) - ord('a')
            freq1[ch1] += 1

            ch2 = ord(word2[i]) - ord('a')
            freq2[ch2] += 1

        for i in range(26):
            if freq1[i] != 0 and freq2[i] != 0:
                continue
            if freq1[i] == 0 and freq2[i] == 0:
                continue
            return False

        return sorted(freq1) == sorted(freq2)
        