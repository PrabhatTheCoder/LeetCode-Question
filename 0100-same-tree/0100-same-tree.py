# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # def level(self, root):
    #     if root is None:
    #         return
            
    #     return 1 + max(self.level(root.left), self.level(root.right))

    def solve(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        if self.solve(p.left, q.left) == False:
            return False
        
        if self.solve(p.right, q.right) == False:
            return False
        
        return True

    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        # level = self.level(root)

        return self.solve(p, q)

        