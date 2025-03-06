# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        temp = head
        i = 1
        while temp and temp.next:
            temp = temp.next
            i += 1
        tail = temp

        k = k%i
        if k == 0:
            return head

        temp = head
        for _ in range(i - k - 1):
            temp = temp.next

        new_head = temp.next
        temp.next = None
        tail.next = head 

        return new_head


        