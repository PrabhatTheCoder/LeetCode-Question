# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # T:C - O(n) and S:C - O(1)
        # Based on Recursion leap of faith

        if not head or not head.next:
            return None

        head = head.next
        temp = head
        sum = 0
        while temp and temp.val != 0:
            sum += temp.val
            temp = temp.next

        head.val = sum
        head.next = self.mergeNodes(temp)
        return head