class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = {}

        # Count frequencies of normalized remainders
        for num in arr:
            remainder = (num % k + k) % k
            dic[remainder] = dic.get(remainder, 0) + 1

        # Check remainder 0 separately (must be even)
        if dic.get(0, 0) % 2 != 0:
            return False

        # Check complementary remainders
        for i in range(1, k // 2 + 1):
            if dic.get(i, 0) != dic.get(k - i, 0):
                return False

        return True
