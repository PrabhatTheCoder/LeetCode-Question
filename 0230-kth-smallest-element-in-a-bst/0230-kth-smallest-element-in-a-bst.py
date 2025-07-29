class Solution:
    def solve(self, root, k, count):
        if not root:
            return None

        # Traverse left subtree
        left = self.solve(root.left, k, count)
        if left is not None:
            return left

        # Visit current node
        count[0] += 1
        if count[0] == k:
            return root.val

        # Traverse right subtree
        return self.solve(root.right, k, count)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Using list so count is mutable across recursive calls
        return self.solve(root, k, [0])
