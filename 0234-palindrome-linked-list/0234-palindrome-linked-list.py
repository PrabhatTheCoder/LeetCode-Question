# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        c = ListNode(-1)
        temp = head
        tempc = c
        while temp:
            node = ListNode(temp.val)
            tempc.next = node
            tempc = tempc.next
            temp = temp.next

        c = self.reverseList(c.next)
        while head:
            if head.val != c.val:
                return False
            head = head.next
            c = c.next
        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

        