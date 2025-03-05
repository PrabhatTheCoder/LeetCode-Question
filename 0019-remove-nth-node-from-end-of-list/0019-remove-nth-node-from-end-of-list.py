class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        slow = head
        fast = head

        for i in range(n+1):
            if fast == None:
                return head.next
            fast = fast.next
        
        while fast != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
        
    