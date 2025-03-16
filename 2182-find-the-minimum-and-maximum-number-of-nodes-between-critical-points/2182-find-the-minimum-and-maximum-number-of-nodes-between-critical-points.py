# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        a = head
        b = head.next
        c = head.next.next
        fdx = -1
        sdx = -1
        idx = 1
        min_dist = float('inf')
        
        while c:
            if (a.val > b.val and b.val < c.val) or (a.val < b.val and b.val > c.val):
                if fdx == -1:
                    fdx = idx
                else:
                    min_dist = min(min_dist, idx - sdx)
                sdx = idx
            
            a = a.next
            b = b.next
            c = c.next
            idx += 1
        
        if fdx == sdx:  # If only one critical point was found
            return [-1, -1]
        
        return [min_dist, sdx - fdx]  # Min and max distances