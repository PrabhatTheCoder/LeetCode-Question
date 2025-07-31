# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pred(self, root):
        if not root:
            return
        if not root.left:
            return
        root = root.left
        while root.right:
            root = root.right

        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:

            # 0 children
            if root.left is None and root.right is None:
                return None
            
            # 1 child
            if root.left is None and root.right is not None:
                return root.right
            if root.right is None and root.left is not None:
                return root.left
            
            # If Node have 2 Child (Predeccesor & Successor)
            if root.left and root.right:

                # Predeccesor
                pred = self.pred(root)
                root.val = pred.val
                root.left = self.deleteNode(root.left, pred.val)
                
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)   
        else:
            root.left = self.deleteNode(root.left, key)
        
        return root
        