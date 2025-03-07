class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = []
        for i in range(n):
            ans = [None] * n
            matrix.append(ans)

        if not matrix or not matrix[0]:
            return []

        minr, maxr = 0, len(matrix) - 1
        minc, maxc = 0, len(matrix[0]) - 1

        k = 1
        while minr <= maxr and minc <= maxc:

            # Move Right
            for i in range(minc, maxc + 1):
                matrix[minr][i] = k
                k += 1
            minr += 1 

            # Move Down
            if minr <= maxr:
                for j in range(minr, maxr + 1):
                    matrix[j][maxc] = k
                    k += 1
                maxc -= 1 

            # Move Left
            if minr <= maxr:
                for i in range(maxc, minc - 1, -1):
                    matrix[maxr][i] = k
                    k += 1
                maxr -= 1  # Move row boundary up

            # Move Up
            if minc <= maxc:
                for l in range(maxr, minr - 1, -1):
                    matrix[l][minc] = k
                    k +=1
                minc += 1  # Move column boundary right

        return matrix

        
        