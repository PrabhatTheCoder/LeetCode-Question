class Solution:

    def reverse(self, word):
        new_word = ''
        for i in range(len(word)-1,-1,-1):
            new_word += word[i]
        return new_word

    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        dic = {}
        count = 0

        for word in words:
            rev_word = self.reverse(word)

            # If reverse exists already → count one pair
            if rev_word in dic:
                count += 1
            else:
                dic[word] = 1   # mark this word as seen

        return count