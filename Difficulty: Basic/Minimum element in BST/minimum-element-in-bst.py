"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

class Solution:
    temp = None
    
    def minValue(self, root):
        if root.left is None:
            return root.data
        return self.minValue(root.left)