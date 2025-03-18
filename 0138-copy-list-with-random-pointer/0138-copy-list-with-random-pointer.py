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
        curr = head
        newHead = Node(-1)
        prev = newHead
        dic = {}

        while curr:
            temp = Node(curr.val)
            dic[curr] = temp

            prev.next = temp

            prev = prev.next
            curr = curr.next

        # Second pass: Set random pointers
        temp = newHead.next
        curr = head
        while temp:
            if curr.random:
                temp.random = dic[curr.random]
            temp = temp.next
            curr = curr.next

        return newHead.next
                     