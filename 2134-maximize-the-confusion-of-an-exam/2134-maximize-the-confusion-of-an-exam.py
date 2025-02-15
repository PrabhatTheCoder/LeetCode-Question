class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i = 0
        j = 0
        k_val = 0
        max_T = 0
        # False to True
        while j < len(answerKey):
            if answerKey[j] == 'F':
                k_val += 1

            while k_val > k:
                if answerKey[i] == 'F':
                    k_val -= 1
                i += 1

            max_T = max(max_T, j-i+1)
            j += 1

        
        i = 0
        j = 0
        k_val = 0
        max_F = 0

        # True to False
        while j < len(answerKey):
            if answerKey[j] == 'T':
                k_val += 1

            while k_val > k:
                if answerKey[i] == 'T':
                    k_val -= 1
                i += 1

            max_F = max(max_F, j-i+1)
            j += 1

        return max(max_T,max_F)
            