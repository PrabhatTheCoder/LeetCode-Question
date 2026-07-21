# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.ans = 0

    def solve(self, root):
        if root is None:
            return 0

        left = self.solve(root.left)
        right = self.solve(root.right)

        self.ans = max(self.ans, left + right)

        return 1 + max(left, right)
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.solve(root)
        return self.ans

        