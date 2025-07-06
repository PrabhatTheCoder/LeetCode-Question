# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if not root:
            return []

        res = []

        stack = []
        stack.append(root)
        while stack:
            temp = stack.pop()
            res.append(temp.val)

            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)

        return res




        