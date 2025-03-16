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
        while temp:
            dummy = ListNode(-1)
            tempC = dummy
            if rem > 0:
                for i in range(size+1):
                    tempC.next = temp
                    temp = temp.next
                    tempC = tempC.next
                tempC.next = None
                rem -= 1
            else:
                for i in range(size):
                    tempC.next = temp
                    temp = temp.next
                    tempC = tempC.next
                tempC.next = None
            ans.append(dummy.next)

        print(len(ans))
        while len(ans) < k:
            ans.append(None)
        return ans

        