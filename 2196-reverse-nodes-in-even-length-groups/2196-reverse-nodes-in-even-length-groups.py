# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        gap = 1
        
        while temp and temp.next:
            remLen = 0
            t = temp.next
            for _ in range(gap+1):
                if not t:
                    break
                t = t.next
                remLen += 1
            
            # If remaining nodes are less than expected, adjust gap size
            if remLen < gap + 1:
                gap = remLen - 1
            
            if (2 + gap) % 2 != 0:  # Reverse if gap is odd or results in an even group
                self.reverseBetween(temp, 2, 2 + gap)
            
            gap += 1
            for _ in range(gap):
                if not temp:
                    break
                temp = temp.next
        
        return head

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
        
        if temp:
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
        