# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(-1)
        prev = newHead
        curr = head
        val = 0
        while curr:
            if curr.val == 0:
                prev.next = ListNode(val)
                val = 0
                prev = prev.next
            else:
                val += curr.val
            curr = curr.next

        return newHead.next.next
        