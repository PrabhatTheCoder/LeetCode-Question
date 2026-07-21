# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def solve(self, root):
        if root is None:
            return None

        temp1 = root.left
        temp2 = root.right

        root.left = temp2
        root.right = temp1

        self.solve(root.left)
        self.solve(root.right)



    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.solve(root)
        return root
        