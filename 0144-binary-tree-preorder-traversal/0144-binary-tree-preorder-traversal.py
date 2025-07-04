# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root: [TreeNode], ans) -> List[int]:
        if not root:
            return

        ans.append(root.val)
        self.dfs(root.left, ans)
        self.dfs(root.right, ans)


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.dfs(root, ans)
        return ans
        