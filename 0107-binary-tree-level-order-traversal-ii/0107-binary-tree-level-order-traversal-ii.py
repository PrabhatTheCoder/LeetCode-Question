# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        height = self.maxLevel(root)
        res = []
        
        for i in range(height-1,-1,-1):
            
            ans = []
            self.solve(root, 0, i, ans)   
            res.append(ans) 
        return res

    def maxLevel(self, root):
        if not root:
            return 0
            
        return 1 + max(self.maxLevel(root.left), self.maxLevel(root.right))
        
    def solve(self, root, curr_level, target_level, ans):
        if not root:
            return

        if curr_level == target_level:
            ans.append(root.val)
            return 
        
        self.solve(root.left, curr_level+1, target_level, ans)
        self.solve(root.right, curr_level+1, target_level, ans)
