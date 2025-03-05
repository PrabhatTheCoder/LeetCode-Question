class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Find the length of the list
        temp = head
        i = 0
        while temp:
            i += 1
            temp = temp.next

        # Step 2: Find the position of the node to remove
        m = i - n  # the index to remove (0-based index)

        # Step 3: If we need to remove the head
        if m == 0:
            return head.next

        # Step 4: Traverse the list again to find the node just before the one to be deleted
        temp = head
        for _ in range(m - 1):
            temp = temp.next

        # Step 5: Remove the nth node from the end
        if temp.next:  # this check is just to be safe
            temp.next = temp.next.next

        return head
