class Solution(object):
    def buildTree(self, inorder, postorder):

        # [9,3,15,20,7]     Left Root Right - Inorder
        # [9,15,7,20,3]     Left Right Root - Postorder

        
        # Map value -> index for inorder
        inorder_index = {val: idx for idx, val in enumerate(inorder)}

        # Postorder pointer (start from end)
        self.post_idx = len(postorder) - 1

        def helper(left, right):
            # No elements in this subtree
            if left > right:
                return None

            # Root is last element in postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            # Split inorder into right and left subtrees
            mid = inorder_index[root_val]

            # Build right subtree first (because postorder is Left-Right-Root)
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)
