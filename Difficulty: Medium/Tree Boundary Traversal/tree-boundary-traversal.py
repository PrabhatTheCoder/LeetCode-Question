'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    
    def leftBoundary(self, root, ans):
        if not root:
            return
    
        if not root.left and not root.right:
            return
    
        ans.append(root.data)
        
        if root.left:
            self.leftBoundary(root.left, ans)
        else:
            self.leftBoundary(root.right, ans)
            
    def rightBoundary(self, root, ans):
        if not root:
            return
        
        if not root.left and not root.right:
            return
        
        if root.right:
            self.rightBoundary(root.right, ans)
        else:
            self.rightBoundary(root.left, ans)
        
        ans.append(root.data)
        
    def bottomBoundary(self, root, ans):
        if not root:
            return
        
        if not root.left and not root.right:
            if root != self.root:
                ans.append(root.data)
            return
        
        self.bottomBoundary(root.left, ans)
        self.bottomBoundary(root.right, ans)

    def boundaryTraversal(self, root):
        self.root = root
        ans = [root.data]
        self.leftBoundary(root.left, ans)
        self.bottomBoundary(root, ans)
        self.rightBoundary(root.right, ans)
        return ans

        
        
        