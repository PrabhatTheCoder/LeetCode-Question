# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        tempA = headA
        tempB = headB

        i = 0
        while tempA != None:
            i += 1
            tempA = tempA.next
            
        j = 0
        while tempB != None:
            j += 1
            tempB = tempB.next

        m = abs(j-i)
        if j>i:
            while m != 0:
                headB = headB.next
                m -= 1
        else:
            while m != 0:
                headA = headA.next
                m -= 1

        while headA is not None and headB is not None:
            if headA == headB:
                return headA  
            headA = headA.next
            headB = headB.next
  

        