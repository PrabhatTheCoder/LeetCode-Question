class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = {}

        # Count frequencies of normalized remainders
        for num in arr:
            remainder = (num % k + k) % k
            if remainder not in dic:
                dic[remainder] = 1
            else:
                dic[remainder] += 1

        # Check remainder 0 separately (must be even)
        if 0 in dic and dic[0] % 2 != 0:
            return False
        elif 0 not in dic:
            dic[0] = 0  # Ensure 0 exists for later checks

        # Check complementary remainders
        for i in range(1, k // 2 + 1):
            if i not in dic:
                dic[i] = 0
            if (k - i) not in dic:
                dic[k - i] = 0

            if dic[i] != dic[k - i]:
                return False

        return True
