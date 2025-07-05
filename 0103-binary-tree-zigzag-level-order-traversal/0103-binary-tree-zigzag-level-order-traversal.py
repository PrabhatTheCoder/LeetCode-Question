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

    def solve(self, root, curr_level, target_level, ans):
        if not root:
            return

        if curr_level == target_level:
            ans.append(root.val)
            return

        self.solve(root.left, curr_level+1, target_level, ans)  # Left
        self.solve(root.right, curr_level+1, target_level, ans) # Right

    def ReverseSolve(self, root, curr_level, target_level, ans):
        if not root:
            return

        if curr_level == target_level:
            ans.append(root.val)
            return

        self.ReverseSolve(root.right, curr_level+1, target_level, ans)  # Right
        self.ReverseSolve(root.left, curr_level+1, target_level, ans)   # Left


    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        height = self.level(root)

        res = []
        for i in range(height):
            ans = []
            if i%2 == 0:
                self.solve(root, 0, i, ans)
            else:
                self.ReverseSolve(root, 0, i, ans)
            res.append(ans)

        return res        