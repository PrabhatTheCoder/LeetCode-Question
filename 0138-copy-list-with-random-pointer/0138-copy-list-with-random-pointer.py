"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {}
        curr = head
        new_curr = Node(-1)
        dummy = new_curr

        while curr:
            node = Node(curr.val)
            new_curr.next = node

            dic[curr] = node
            new_curr = new_curr.next
            curr = curr.next


        new_curr = dummy.next
        curr = head
        while curr:
            if curr.random == None:
                new_curr.random = None
            else:
                new_curr.random = dic[curr.random]
            new_curr = new_curr.next
            curr = curr.next

        return dummy.next

