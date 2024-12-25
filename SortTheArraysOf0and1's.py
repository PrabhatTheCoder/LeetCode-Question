class Solution():
    
    def SortTheArraysOf0and1(self, nums):
        i = 0
        j = len(nums) - 1
        
        while i < j:
            if nums[i] == 1 and nums[j] == 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1
            elif nums[i] == 0:
                i += 1
            elif nums[j] == 1:
                j -= 1
            else:
                i += 1
                j -= 1
        return nums
                
        



nums = [0,1,0,0,1,1,0,1]
s = Solution()
ans = s.SortTheArraysOf0and1(nums)
print(ans)
