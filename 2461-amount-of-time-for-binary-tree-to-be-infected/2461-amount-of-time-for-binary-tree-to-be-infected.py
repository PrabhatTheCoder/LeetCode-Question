# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, start):
        if not root:
            return 0 
        
        left_height = self.solve(root.left, start)
        right_height = self.solve(root.right, start)

        if root.val == start:
            # Found start node
            self.result = max(left_height, right_height)
            return -1
        
        # Normal upward height propagation
        elif left_height >= 0 and right_height >= 0:
            return 1 + max(left_height, right_height)
        
        else:
            # One of the child paths contains the start node
            d = abs(left_height) + abs(right_height)
            self.result = max(self.result, d)
            return min(left_height, right_height) - 1

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.result = 0   # Reset result for each test case
        self.solve(root, start)
        return self.result
