class Solution:
        def countAndSay(self, n: int) -> str:
            if n == 1:
                return "1"

            nums = str(self.countAndSay(n-1))   # nums = "23 32 15 11"
            result = ""
            freq = 1
            char = nums[0]
            for i in range(1,len(nums)):
                if char == nums[i]:
                    freq += 1
                else:
                    result += str(freq) + char
                    freq = 1
                    char = nums[i]
            result += str(freq) + char
            return result