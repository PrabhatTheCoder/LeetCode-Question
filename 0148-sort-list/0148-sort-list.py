# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        b = slow.next
        slow.next = None

        a = self.sortList(head)
        b = self.sortList(b)
        return self.mergeTwoLists(a,b)


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        temp3 = ListNode(-1)
        c = temp3

        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp3.next = temp1
                temp1 = temp1.next
                temp3 = temp3.next
            else:
                temp3.next = temp2
                temp2 = temp2.next
                temp3 = temp3.next


        if temp1 == None:
            temp3.next = temp2
        if temp2 == None:
            temp3.next = temp1

        return c.next
        
        