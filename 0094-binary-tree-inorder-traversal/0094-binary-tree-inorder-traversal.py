# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pred = None
        visited = []
        curr = root

        while curr != None:

            # If root->left exists
            if curr.left != None:
                pred = curr.left

                while pred.right and pred.right != curr:
                    pred = pred.right

                # Link
                if pred.right == None:
                    pred.right = curr
                    curr = curr.left

                # Unlink - If pred->right = curr
                if pred.right == curr:
                    visited.append(curr.val)
                    curr = curr.right
                    pred.right = None

            # If root->left not exists
            else:
                visited.append(curr.val)
                curr = curr.right

        return visited
            
                

            
