class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                if len(stack) >= 2:
                    val1 = stack[-1]
                    val2 = stack[-2]
                    stack.append(val1 + val2)
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                if stack:
                    stack.append(2*stack[-1])
            else:
                try:
                    stack.append(int(op))
                except ValueError:
                    pass
        return sum(stack)
        