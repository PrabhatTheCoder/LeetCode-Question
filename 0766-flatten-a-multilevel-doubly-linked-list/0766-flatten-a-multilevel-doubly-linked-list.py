"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        
        stack = []
        curr = head
        tail = head
        while curr:
            if curr.child:
                if curr.next:
                    curr.next.prev = None
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            tail = curr
            curr = curr.next


        while stack:
            curr = stack.pop()
            tail.next = curr
            curr.prev = tail
            while curr:
                tail = curr
                curr = curr.next
            
        return head
                    
        