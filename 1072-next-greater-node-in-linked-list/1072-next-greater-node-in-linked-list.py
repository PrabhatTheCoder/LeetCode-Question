# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def NearestLargerToLeft(self, head) -> int:
        pseudo_idx = 0
        stack = []
        ans = []
        
        i = 1
        while head:

            if not stack:
                ans.append(pseudo_idx)

            elif stack and stack[-1][0] > head.val:
                ans.append(stack[-1][0])

            elif stack and stack[-1][0] <= head.val:
                while stack and stack[-1][0] <= head.val:
                    stack.pop()

                if not stack:
                    ans.append(pseudo_idx)
                else:
                    ans.append(stack[-1][0])
            
            stack.append((head.val, i))
            head = head.next
            i += 1

        return ans

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        head = self.reverseList(head)
        ans = self.NearestLargerToLeft(head)
        ans.reverse()
        return ans

        