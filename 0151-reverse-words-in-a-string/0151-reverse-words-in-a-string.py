class Solution:

    def rotateString(self, s):
        newS = ""
        for i in range(len(s)-1, -1, -1):
            newS += s[i]
        return newS

    def reverseWords(self, s: str) -> str:
        newW = ""
        words = []

        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if newW: 
                    words.append(self.rotateString(newW))
                    newW = ""
            else:
                newW += s[i]

        if newW:
            words.append(self.rotateString(newW))

        return " ".join(words)
