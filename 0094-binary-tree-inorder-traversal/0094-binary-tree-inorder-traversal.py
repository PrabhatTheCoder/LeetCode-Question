class Solution(object):

    def solve(self, root, ans):
        if root is None:
            return

        self.solve(root.left, ans)
        ans.append(root.val)
        self.solve(root.right, ans)

    def inorderTraversal(self, root):
        ans = []
        self.solve(root, ans)
        return ans