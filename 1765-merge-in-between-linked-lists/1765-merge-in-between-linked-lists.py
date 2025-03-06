# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        j = 0
        temp = list1
        while temp:
            if j == b+1:
                val = temp
                break
            j += 1
            temp = temp.next
        

        temp1 = list1
        i = 1
        while temp1:
            if i == a:
                temp1.next = list2

            i += 1
            temp1 = temp1.next

        while list2.next:
            list2 = list2.next

        list2.next = val
        return list1
