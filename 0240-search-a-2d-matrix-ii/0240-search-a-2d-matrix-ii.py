class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        # Start from the top-right corner
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = col - 1


        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1  # Move left
            else:
                i += 1

        return False
        