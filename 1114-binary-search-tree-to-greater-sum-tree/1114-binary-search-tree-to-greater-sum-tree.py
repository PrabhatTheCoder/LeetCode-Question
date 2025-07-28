# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0  

    def reverse_inorder(self, node):
        if not node:
            return

        self.reverse_inorder(node.right)

        self.total += node.val
        node.val = self.total

        self.reverse_inorder(node.left)

        
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverse_inorder(root)
        return root

        
        