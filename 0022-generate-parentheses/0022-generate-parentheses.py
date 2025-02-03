class Solution:

    def solve(self,val,open_count,close_count,result):
        if open_count == 0 and close_count == 0:
            result.append(val)
            return

        if open_count != 0:
            val1 = val + "("
            self.solve(val1,open_count-1,close_count,result)

        if close_count > open_count:
            val2 = val + ")"
            self.solve(val2,open_count,close_count-1,result)
            
            

    def generateParenthesis(self, n: int) -> List[str]:
        open_count = n
        close_count = n
        result = []
        val = ""
        self.solve(val,open_count,close_count,result)
        return result

