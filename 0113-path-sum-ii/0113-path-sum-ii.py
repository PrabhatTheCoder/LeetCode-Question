# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def solve(self, root, total_val, targetSum, ans, res):
        if not root:
            return

        # Add current node value
        total_val += root.val
        ans.append(root.val)

        # Check if it's a leaf and sum matches
        if total_val == targetSum and not root.left and not root.right:
            res.append(list(ans))  # append a copy
        else:
            self.solve(root.left, total_val, targetSum, ans, res)
            self.solve(root.right, total_val, targetSum, ans, res)

        # Backtrack
        ans.pop()

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        self.solve(root, 0, targetSum, [], res)
        return res
