# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def removeNode(self, head, n):
        idx = 0
        dummy = ListNode(-1)
        dummy.next = head

        temp = dummy
        while temp:
            
            if idx == n:
                prev.next = temp.next
            idx += 1
            prev = temp
            temp = temp.next
            
        return dummy.next

    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next     # save next node
            curr.next = prev     # reverse link
            prev = curr          # move prev
            curr = temp          # move curr

        return prev   # new head

        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.reverseList(head)
        temp = self.removeNode(head, n)
        return self.reverseList(temp)



        