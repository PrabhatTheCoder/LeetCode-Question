class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        columns = len(matrix[0])
        result = [[0] * rows for _ in range(columns)] 

        for row in range(rows):
            for column in range(columns):
                result[column][row] = matrix[row][column] 
        
        return result