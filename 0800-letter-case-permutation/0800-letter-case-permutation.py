class Solution:

    def solve(self, op , inp, result):
        if len(inp) == 0:
            return result.append(op)

        if inp[0].isalpha():
            op1 = op + inp[0].lower() 
            op2 = op + inp[0].upper() 
            self.solve(op1, inp[1:], result)
            self.solve(op2, inp[1:], result) 
        else:
            # If it's not a letter, just append it as it is
            self.solve(op + inp[0], inp[1:], result)


    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        self.solve("",s,result)

        return result

        