class Solution:

    def reverse(self, n):
        r = 0   # 123
        while n > 0:
            r *= 10
            r += (n%10)
            n = n // 10
        return r

    def countDistinctIntegers(self, nums: List[int]) -> int:
        dic = {}

        for i in range(len(nums)):
            nums.append(self.reverse(nums[i]))
        
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1

        return len(dic)
            