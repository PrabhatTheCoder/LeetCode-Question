# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = last = head
        for i in range(1,k):
            first = first.next
        
        NullChecker = first
        while NullChecker.next:
            NullChecker = NullChecker.next
            last = last.next
            
        first.val, last.val = last.val, first.val
        return head

