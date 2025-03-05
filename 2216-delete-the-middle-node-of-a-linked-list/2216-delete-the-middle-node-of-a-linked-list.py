# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None  # Edge case: Single node list should return None
            
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        temp = head
        while temp.next != slow:
            temp = temp.next

        temp.next = temp.next.next

        return head
        