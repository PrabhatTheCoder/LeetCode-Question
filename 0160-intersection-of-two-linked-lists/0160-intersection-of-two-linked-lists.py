# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        temp = headA
        while temp:
            lenA += 1
            temp = temp.next

        temp = headB
        while temp:
            lenB += 1
            temp = temp.next

        # Align heads
        diff = abs(lenA - lenB)
        temp1, temp2 = headA, headB

        if lenA > lenB:
            for _ in range(diff):
                temp1 = temp1.next
        else:
            for _ in range(diff):
                temp2 = temp2.next

        # Move together until intersection
        while temp1 and temp2:
            if temp1 == temp2:   # must be same node, not just same value
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next

        return None
