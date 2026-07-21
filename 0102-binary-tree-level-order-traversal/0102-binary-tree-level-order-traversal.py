# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def solve(self, root, i, j, ans):
        if root is None:
            return

        if i == j:
            ans.append(root.val)
            return

        self.solve(root.left, i, j+1, ans)
        self.solve(root.right, i, j+1, ans)

        return

    def depth(self, root):
        if root is None:
            return 0

        return 1 + max(self.depth(root.left), self.depth(root.right))

    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        depth = self.depth(root)
        res = []
        for i in range(depth):
            ans = []
            self.solve(root, i, 0, ans)
            res.append(ans)

        return res