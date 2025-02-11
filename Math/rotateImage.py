class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        r = 0
        cc = 0

        # Transposing the matrix
        while r != rows:

            for c in range(cc, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

            r += 1
            cc += 1
        
        print(matrix)
        
        # Reflection of the matrix

        
        # 00 -> 03
        # 10 -> 12

        # 01 -> 02

        for r in range(rows):

            for c in range(cols//2):

                matrix[r][c], matrix[r][cols - c - 1] = matrix[r][cols - c - 1],  matrix[r][c]
