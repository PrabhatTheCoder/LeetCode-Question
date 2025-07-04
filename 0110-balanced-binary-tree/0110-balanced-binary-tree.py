# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def Maxlevel(self, root):

        if not root:
            return 0
        return 1 + max(self.Maxlevel(root.left),  self.Maxlevel(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        left_height = self.Maxlevel(root.left)
        right_height = self.Maxlevel(root.right)

        if abs(left_height - right_height) > 1:
                    return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
