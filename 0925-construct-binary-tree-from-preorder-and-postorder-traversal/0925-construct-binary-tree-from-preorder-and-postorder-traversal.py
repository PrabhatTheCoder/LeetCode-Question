class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        postorder_index = {val: idx for idx, val in enumerate(postorder)}
        self.pre_idx = 0

        def helper(left, right):
            
            if left > right:
                return None

            # Create root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # If leaf node
            if left == right:
                return root

            # Next value in preorder is left child
            left_child_val = preorder[self.pre_idx]
            mid = postorder_index[left_child_val]

            # Build left and right subtrees
            root.left = helper(left, mid)
            root.right = helper(mid + 1, right - 1)  # exclude root in postorder

            return root

        return helper(0, len(postorder) - 1)
