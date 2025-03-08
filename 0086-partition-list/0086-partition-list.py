# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy
        greater = greater_dummy
        temp = head

        while temp:
            if temp.val < x:
                less.next = temp
                less = less.next
            else:
                greater.next = temp
                greater = greater.next
            temp = temp.next

        # Connect the two lists
        greater.next = None
        less.next = greater_dummy.next

        return less_dummy.next

        