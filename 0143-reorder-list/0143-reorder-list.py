# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tempa = head
        tempb = slow.next
        slow.next = None
        tempb = self.reverseList(tempb)

        mergeList = self.mergeTwoLists(tempa,tempb)
        return mergeList

        


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Recurion
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        temp3 = ListNode(-1)
        c = temp3

        while temp1 and temp2:
            temp3.next = temp1
            temp1 = temp1.next
            temp3 = temp3.next
            temp3.next = temp2
            temp2 = temp2.next
            temp3 = temp3.next


        if temp1 == None:
            temp3.next = temp2
        if temp2 == None:
            temp3.next = temp1

        return c.next
        