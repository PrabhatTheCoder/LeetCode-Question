class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        sumArray = [0]*len(nums)
        sumArray[0] = nums[0]
        for i in range(1,len(nums)):
            sumArray[i] = sumArray[i-1] + nums[i]
        self.sumArray = sumArray

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            leftVal = 0
        else:
            leftVal = self.sumArray[left-1]
        ans = self.sumArray[right] - leftVal
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)