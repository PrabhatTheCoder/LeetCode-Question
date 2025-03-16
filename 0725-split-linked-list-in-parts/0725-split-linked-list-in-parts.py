# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        # Find the length of LL
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n += 1
        
        # Breaking the LL
        size = n//k
        rem = n%k
        
        temp = head
        ans = []
        for _ in range(k):
            dummy = ListNode(-1)  # Dummy head
            tempC = dummy
            
            # Set the correct partition size
            part_size = size + (1 if rem > 0 else 0)
            rem -= 1  # Decrease remaining extra nodes
            
            for _ in range(part_size):
                if temp:
                    tempC.next = temp
                    tempC = temp
                    temp = temp.next
            
            # Break the link to the next part
            if tempC:
                tempC.next = None
            
            ans.append(dummy.next)
        
        return ans