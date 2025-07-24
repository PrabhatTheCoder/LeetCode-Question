# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    
    prev = None
    flag = True
    def Inorder(self, root):
        if not root:
            return
        left = self.Inorder(root.left)

        if self.prev != None:
            if root.val <= self.prev:
                self.flag = False
                return
        self.prev = root.val
        
        right = self.Inorder(root.right)

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.Inorder(root)
        return self.flag
        
        