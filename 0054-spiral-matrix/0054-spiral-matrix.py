class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        minr = 0
        maxr = len(matrix) - 1
        minc = 0
        maxc = len(matrix[0]) - 1
        res = []

        while minr <= maxr and minc <= maxc:
            # Traverse right
            for i in range(minc, maxc + 1):
                res.append(matrix[minr][i])
            minr += 1
            
            # Traverse down
            for i in range(minr, maxr + 1):
                res.append(matrix[i][maxc])
            maxc -= 1
            
            if minr <= maxr:
                # Traverse left
                for i in range(maxc, minc - 1, -1):
                    res.append(matrix[maxr][i])
                maxr -= 1

            if minc <= maxc:
                # Traverse up
                for i in range(maxr, minr - 1, -1):
                    res.append(matrix[i][minc])
                minc += 1

        return res
