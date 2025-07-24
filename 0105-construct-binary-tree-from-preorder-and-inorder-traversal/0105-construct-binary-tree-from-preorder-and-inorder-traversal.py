# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # [1,2,4,5,3,6]     Root Left Right - Proder
        # [4,2,5,1,3,6]     Left Root Right - Inorder
        
        # **Base case**
        if not preorder or not inorder:
            return None
        
        for i in range(len(inorder)):
            if preorder[0] == inorder[i]:
                Node = TreeNode(preorder[0])

                length_left = len(inorder[:i])  # left subtree size
                left_inorder = inorder[:i]
                left_preorder = preorder[1:length_left + 1]

                length_right = len(inorder[i + 1:])
                right_inorder = inorder[i + 1:]
                right_preorder = preorder[length_left + 1:]

                left_Tree = self.buildTree(left_preorder, left_inorder)
                right_Tree = self.buildTree(right_preorder, right_inorder)

                Node.left = left_Tree
                Node.right = right_Tree

                return Node  # **Return immediately after constructing**