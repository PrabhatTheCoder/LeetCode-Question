# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def solve(self, root, ans):
        if root is None:
            return []

        ans.append(root.val)

        self.solve(root.left, ans)
        self.solve(root.right, ans)

        return ans
        

    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        ans = []
        return self.solve(root, ans)
        