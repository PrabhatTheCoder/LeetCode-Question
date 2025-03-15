# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)   # Even List
        EvenList = dummy
        
        dummy2 = ListNode(-1)   # Odd List
        dummy2.next = head
        head = dummy2
        temp = head

        i = 1

        while temp and temp.next:
            if i % 2 == 0:  # Even
                EvenList.next = temp.next
                temp.next = temp.next.next
                EvenList.next.next = None
                EvenList = EvenList.next
            else:
                temp = temp.next
            i += 1
        temp.next = dummy.next
        return head.next



        