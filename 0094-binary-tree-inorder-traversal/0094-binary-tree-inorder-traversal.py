# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        ans = []
        node = root
        stack = []

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                temp = stack.pop()
                ans.append(temp.val)
                node = temp.right

        return ans
        