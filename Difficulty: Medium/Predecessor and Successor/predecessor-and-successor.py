'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    
    def findPreSuc(self, root, key):
        self.pre = None
        self.suc = None

        def inorder(node):
            if not node:
                return

            # Left subtree
            inorder(node.left)

            # Update predecessor and successor dynamically
            if node.data < key:
                self.pre = node
            elif node.data > key and self.suc is None:
                self.suc = node

            # Right subtree
            inorder(node.right)

        inorder(root)
        return self.pre, self.suc
