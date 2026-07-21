# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def level(self, root):
        if root is None:
            return 0

        return 1 + max(self.level(root.left), self.level(root.right))

    def solve(self, root, ans, level, curr):
        if root is None:
            return
        
        if level == curr:
            ans.append(root.val)
            return
        
        self.solve(root.left, ans, level, curr + 1)
        self.solve(root.right, ans, level, curr + 1)


    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        level = self.level(root)
        res = []

        for i in range(level):
            ans = []
            self.solve(root, ans, i, 0)
            if ans:
                res.append(ans[-1])

        return res


        