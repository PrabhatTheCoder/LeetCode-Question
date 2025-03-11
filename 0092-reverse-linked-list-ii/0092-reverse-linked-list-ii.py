# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        i = 1
        left_pos = None
        left_val = None
        right_pos = None

        # Find left and right positions
        while temp and temp.next:
            if i == left - 1:
                left_val = temp
                left_pos = temp.next
            if i == right:
                right_pos = temp.next
                temp.next = None
                break
            i += 1
            temp = temp.next

        # If left_pos is not set, it means we're reversing from the head
        if not left_pos:
            left_pos = head

        reverseList = self.reverseList(left_pos)

        if left_val:
            left_val.next = reverseList
        else:
            head = reverseList  # If left == 1, update head

        temp = reverseList
        while temp and temp.next:
            temp = temp.next
        
        temp.next = right_pos

        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev