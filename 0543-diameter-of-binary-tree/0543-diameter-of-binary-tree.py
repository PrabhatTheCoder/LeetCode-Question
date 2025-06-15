# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0  # Height of an empty tree is 0
            
            left_height = helper(node.left)
            right_height = helper(node.right)
            
            # Update the maximum diameter at this node
            self.maxDia = max(self.maxDia, left_height + right_height)
            
            # Return the height of this subtree
            return 1 + max(left_height, right_height)
        
        self.maxDia = 0
        helper(root)  # Start traversal
        return self.maxDia
