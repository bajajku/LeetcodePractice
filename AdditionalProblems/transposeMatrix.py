class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        res = [[0] * ROWS for _ in range(COLS)]

        for c in range(COLS):
            for r in range(ROWS):

                res[c][r] = matrix[r][c]        

        
        return res
