class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        minr, maxr = 0, len(matrix) - 1
        minc, maxc = 0, len(matrix[0]) - 1
        ans = []

        while minr <= maxr and minc <= maxc:

            # Move Right
            for i in range(minc, maxc + 1):
                ans.append(matrix[minr][i])
            minr += 1  # Move row boundary down

            # Move Down
            for j in range(minr, maxr + 1):
                ans.append(matrix[j][maxc])
            maxc -= 1  # Move column boundary left

            # Move Left
            if minr <= maxr:
                for k in range(maxc, minc - 1, -1):
                    ans.append(matrix[maxr][k])
                maxr -= 1  # Move row boundary up

            # Move Up
            if minc <= maxc:
                for l in range(maxr, minr - 1, -1):
                    ans.append(matrix[l][minc])
                minc += 1  # Move column boundary right

        return ans

        