# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = self.reverseList(slow.next)

        temp_left = head
        temp_right = slow.next
        res = -1
        while temp_right:
            val = temp_left.val + temp_right.val
            if val > res :
                res = val 
            temp_left = temp_left.next
            temp_right = temp_right.next 

        return res

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

        