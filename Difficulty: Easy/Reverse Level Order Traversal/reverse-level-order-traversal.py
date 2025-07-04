'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    
    def maxLevel(self, root):
        if not root:
            return 0
            
        return 1 + max(self.maxLevel(root.left), self.maxLevel(root.right))
        
    def solve(self, root, curr_level, target_level, ans):
        if not root:
            return

        if curr_level == target_level:
            ans.append(root.data)
            return 
        
        self.solve(root.left, curr_level+1, target_level, ans)
        self.solve(root.right, curr_level+1, target_level, ans)

        
        
    def reverseLevelOrder(self,root):
        if not root:
            return
        
        height = self.maxLevel(root)
        res = []
        
        for i in range(height-1,-1,-1):
            
            ans = []
            self.solve(root, 0, i, ans)   
            res.extend(ans)
            
        return res