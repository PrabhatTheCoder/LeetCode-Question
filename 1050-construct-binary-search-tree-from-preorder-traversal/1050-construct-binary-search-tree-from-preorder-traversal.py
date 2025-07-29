# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildBST(self, root, val):
        if not root:
            return None

        if val <= root.val:
            left = self.buildBST(root.left, val)
            if left == None:
                node = TreeNode(val)
                root.left = node
        else:
            right = self.buildBST(root.right, val)
            if right == None:
                node = TreeNode(val)
                root.right = node

        return root
        

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            self.buildBST(root, preorder[i])
        return root

        
        
        