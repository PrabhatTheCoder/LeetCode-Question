# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = [root]
        result = []
        while queue:
            level_size = len(queue)
            ans = []

            for _ in range(level_size):
                node = queue.pop(0)  # pop from front (acts as a queue)
                ans.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(ans)

        return result

                