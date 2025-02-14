class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = 0
        
        vowels = ['a','e','i','o','u']
        Vcount = 0
        maxCount = 0
        while j < len(s):
            # calculation
            if s[j] in vowels:
                Vcount += 1

            if j-i+1 == k:
                maxCount = max(Vcount,maxCount)

                # slide the window
                if s[i] in vowels:
                    Vcount -= 1
                i += 1
                

            j += 1

        return maxCount
        