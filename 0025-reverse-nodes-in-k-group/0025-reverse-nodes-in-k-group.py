# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        cnt = 0

        # check if k nodes exist
        while cnt < k:
            if temp == None:
                return head
            temp = temp.next
            cnt += 1

        # recursively call for rest of LL
        prevNode = self.reverseKGroup(temp, k)


        # reverse current group
        temp = head
        cnt = 0
        while cnt < k:
            next_node = temp.next
            temp.next = prevNode

            prevNode = temp
            temp = next_node
            cnt += 1

        return prevNode
        