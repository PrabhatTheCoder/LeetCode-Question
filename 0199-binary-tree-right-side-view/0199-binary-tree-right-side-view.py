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
        return 1 + max(self.level(root.left), self.level(root.right))

    def solve(self, root, level, target_level, ans):
        if not root:
            return
        if level == target_level:
            ans.append(root.val)
            return
        
        self.solve(root.left, level + 1, target_level, ans)
        self.solve(root.right, level + 1, target_level, ans)

    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        max_level = self.level(root)
        res = []

        for i in range(max_level):
            ans = []
            self.solve(root, 0, i, ans)
            if ans:             
                res.append(ans[-1])
        
        return res
