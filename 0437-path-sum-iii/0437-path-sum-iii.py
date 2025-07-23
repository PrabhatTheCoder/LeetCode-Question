# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def Path_Sum_2(self, root, total_val, targetSum):
        if not root:
            return 0

        # Add current node value
        total_val += root.val

        # Count this path if it matches targetSum
        count = 1 if total_val == targetSum else 0

        # Explore left and right paths continuing from this node
        count += self.Path_Sum_2(root.left, total_val, targetSum)
        count += self.Path_Sum_2(root.right, total_val, targetSum)

        return count

    def solve(self, root, targetSum):
        if not root:
            return 0

        # Count paths starting at current node
        count = self.Path_Sum_2(root, 0, targetSum)

        # Recurse for left and right subtrees
        count += self.solve(root.left, targetSum)
        count += self.solve(root.right, targetSum)

        return count

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.solve(root, targetSum)
        