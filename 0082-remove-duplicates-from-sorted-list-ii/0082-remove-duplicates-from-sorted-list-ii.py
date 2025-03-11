# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode(-1)
        l.next = head
        r = head
        c = l

        while r and r.next:
            if r.val != r.next.val:
                r = r.next
                l = l.next
            else:
                while r.next and r.val == r.next.val:
                    r.next = r.next.next
                l.next = r.next
                r = r.next
        return c.next
        