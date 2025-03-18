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
        # Time - O(1) and Space - O(1)

        if head == None:
            return None
            
        # 1 - Inserting Node in the Middle of LL
        curr = head
        temp = None
        while curr:
            temp = Node(curr.val)
            temp.next = curr.next
            curr.next = temp
            curr = curr.next.next

        # Inserting Random Pointer
        curr = head
        while curr and curr.next:
            if curr.random == None:
                curr.next.random = None
            else:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Removing answer LL
        curr = head
        newHead = head.next
        newCurr = newHead
        while curr:
            curr.next = curr.next.next if curr.next else None
            newCurr.next = newCurr.next.next if newCurr.next else None

            curr = curr.next
            newCurr = newCurr.next

        return newHead
                     