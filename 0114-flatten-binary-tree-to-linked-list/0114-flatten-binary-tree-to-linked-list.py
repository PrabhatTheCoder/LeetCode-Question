# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, ans):
        if not root:
            return
        
        ans.append(root)
        self.preorder(root.left, ans)
        self.preorder(root.right, ans)
        return ans


    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        ans = self.preorder(root,[])
        i = 0
        while i+1 < len(ans):
            ans[i].left = None
            ans[i].right = ans[i+1]
            i += 1
        ans[i].left = None
        ans[i].right = None
        return ans[0]
        
        