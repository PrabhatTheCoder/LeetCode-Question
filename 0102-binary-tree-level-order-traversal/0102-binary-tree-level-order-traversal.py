# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

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
        
        self.solve(root.left, curr_level+1, target_level, ans)
        self.solve(root.right, curr_level+1, target_level, ans)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = self.level(root)
        res = []
        for i in range(level):
            ans = []
            self.solve(root, 0, i, ans)
            res.append(ans)

        return res


        