# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def ReverseLinkedList(self,head):

        # Time Complexity: \U0001d442(\U0001d45b)
        # Space Complexity: \U0001d442(1)

        prev = None
        temp = head
        while temp:
            right = temp.next
            temp.next = prev
            prev = temp
            temp = right
        head = prev
        return head

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.ReverseLinkedList(head)
        dummy = ListNode(-1)
        curr = dummy
        temp = head
        max_val = float('-inf')

        while temp:
            if temp.val >= max_val:
                curr.next = temp
                curr = curr.next
                max_val = temp.val
            temp = temp.next
        
        curr.next = None
        head = self.ReverseLinkedList(dummy.next)
        return head
        