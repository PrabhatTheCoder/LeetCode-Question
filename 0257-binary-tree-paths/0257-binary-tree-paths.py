# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, root, st, ans):
        if not root:
            return

        if st == "":
            st = str(root.val)
        else:
            st += "->" + str(root.val)

        if not root.left and not root.right:
            ans.append(st)
            print(ans)
            return
        
        self.helper(root.left, st, ans)
        self.helper(root.right, st, ans)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        st = ""
        self.helper(root, st, ans)
        return ans
        