class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i==j or j==k or i==k:
                        continue
                    if digits[i] == 0:
                        continue
                    if digits[k] % 2 == 0:
                        val = (digits[i] * 100) + (digits[j] * 10) + digits[k]
                        res.add(val)

        res = list(res)
        res.sort()
        return res
        