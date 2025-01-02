class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # transpose
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        # reverse an array
        for k in range(len(matrix)):
            i = 0
            j = len(matrix)-1
            while i < j:
                matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
                i += 1
                j -= 1

        