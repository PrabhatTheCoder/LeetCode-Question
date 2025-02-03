
class Solution:
    def __init__(self):
        self.result = []  # Initialize result as an instance variable

    def solve(self, val: str, open_count: int, close_count: int) -> None:
        if open_count == 0 and close_count == 0:
            self.result.append(val)
            return

        if open_count > 0:
            self.solve(val + "(", open_count - 1, close_count)

        if close_count > open_count:
            self.solve(val + ")", open_count, close_count - 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []  # Reset result for each call
        self.solve("", n, n)  # Start with n open and close parentheses
        return self.result
