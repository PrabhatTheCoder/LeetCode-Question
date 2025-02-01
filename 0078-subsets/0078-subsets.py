class Solution:

    def solve(self, op, inp, result):
        if len(inp) == 0: 
            result.append(op) 
            return
        
        # Recursive calls
        # 1. Exclude the current character
        self.solve(op, inp[1:], result)

        # 2. Include the current character
        self.solve(op + [inp[0]], inp[1:], result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        self.solve([], nums, result)
        result.sort() 
        return result 
        