class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ")":"(","]":"[","}":"{"
        }
        opening_bracket = ("(","[","{")
        for c in s:
            if c in opening_bracket:
                stack.append(c)
            elif stack and stack[-1] == bracket_map[c]:
                stack.pop()
            else:
                return False
            
        if stack:
            return False
        else:
            return True
        