# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        # print(lists[-1])
        while len(lists) > 1:
            a = lists.pop()
            b = lists.pop()
            c = self.mergeTwoLists(a,b)
            lists.append(c)

        return lists[0]

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

        