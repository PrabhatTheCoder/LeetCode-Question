# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        matrix = []
        for i in range(m):
            ans = [-1] * n
            matrix.append(ans)

        if not matrix or not matrix[0]:
            return []

        minr, maxr = 0, len(matrix) - 1
        minc, maxc = 0, len(matrix[0]) - 1

        temp = head
        while minr <= maxr and minc <= maxc:

            # Move Right
            for i in range(minc, maxc + 1):
                if temp == None:
                    return matrix
                matrix[minr][i] = temp.val
                temp = temp.next
            minr += 1 

            # Move Down
            if minr <= maxr:
                for j in range(minr, maxr + 1):
                    if temp == None:
                        return matrix
                    matrix[j][maxc] = temp.val
                    temp = temp.next
                maxc -= 1 

            # Move Left
            if minr <= maxr:
                for i in range(maxc, minc - 1, -1):
                    if temp == None:
                        return matrix
                    matrix[maxr][i] = temp.val
                    temp = temp.next
                maxr -= 1  # Move row boundary up

            # Move Up
            if minc <= maxc:
                for l in range(maxr, minr - 1, -1):
                    if temp == None:
                        return matrix
                    matrix[l][minc] = temp.val
                    temp = temp.next
                minc += 1  # Move column boundary right

        return matrix

        