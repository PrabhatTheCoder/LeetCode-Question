# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def trim(self, root, low, high):
        if not root:
            return

        while root.left:
            if root.left.val < low:
                root.left = root.left.right
            elif root.left.val > high:
                root.left = root.left.left
            else:
                break   

        while root.right:
            if root.right.val > high:
                root.right = root.right.left
            elif root.right.val < low:
                root.right = root.right.right
            else:
                break

        self.trim(root.left, low, high)
        self.trim(root.right, low, high)
        return root

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        dummy = TreeNode(float('inf'))
        dummy.left = root
        self.trim(dummy, low, high)
        return dummy.left
        