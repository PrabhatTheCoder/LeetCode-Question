class Solution:

    def solve(self, op, inp, result):
        if len(inp) == 0:
            result.add(tuple(op))
            return
        
        # Recursive calls
        # 1. Exclude the current character
        self.solve(op, inp[1:], result)
        
        # 2. Include the current character
        self.solve(op + [inp[0]], inp[1:], result)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        self.solve([], nums, result)
        return [list(subset) for subset in sorted(result)]
        