class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        nums = [0]*10

        for idx in digits:
            nums[idx] += 1

        print(nums)
        
        for i in range(1,10):
            if nums[i] == 0:
                continue
            nums[i] -= 1

            for j in range(10):
                if nums[j] == 0:
                    continue
                nums[j] -= 1

                for k in range(0,9,2):
                    if nums[k] == 0:
                        continue
                    nums[k] -= 1

                    val = (i * 100) + (j * 10) + k
                    res.append(val)

                    nums[k] += 1

                nums[j] += 1

            nums[i] += 1

        return res
        