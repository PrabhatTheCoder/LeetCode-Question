class Solution:

    def reverse(self, digit):
        rev_digit = 0
        while digit > 0:
            rev_digit *= 10
            val = digit % 10
            rev_digit += val
            digit = digit // 10
        return rev_digit

    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        sub_val = []
        for i in range(len(nums)):
            temp = nums[i] - self.reverse(nums[i])
            sub_val.append(temp)

        dic = {}
        for i in range(len(sub_val)):
            if sub_val[i] not in dic:
                dic[sub_val[i]] = 1
            else:
                dic[sub_val[i]] += 1
            
        count_val = 0
        for key in dic:
            freq = dic[key]
            count_val += (freq * (freq - 1)) // 2
            count_val %= MOD
        
        return count_val
        