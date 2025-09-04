# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def level(self, root):
        if not root:
            return 0
        left = self.level(root.left)
        right = self.level(root.right)
        return 1 + max(left, right)

    def solve(self, root, i, target):
        if not root:
            return []
        if i == target:
            return [root.val]

        left = self.solve(root.left, i+1, target)
        right = self.solve(root.right, i+1, target)

        return left + right

    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans = []
        height = self.level(root)

        for i in range(height):
            val = self.solve(root, 0, i)
            ans.append(val)

        return ans
