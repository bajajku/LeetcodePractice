class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        '''three things:
        
            -> Check in same row, 
            -> check in same col
            -> check in same diagonal
        
        '''

        ROWS, COLS = n, n

        rows = set()        
        cols = set()

        leftDiagonal = set()
        rightDiagonal = set()

        res = []

        board = [["."] * COLS for _ in range(ROWS)]

        def isValid(r, c):
            return (
                r not in rows and
                c not in cols and
                (r-c) not in leftDiagonal and
                (r+c) not in rightDiagonal
            )

        
        def function(r):

            if(r == ROWS):
                copy = ["".join(row) for row in board]
                res.append(copy[:])
                return
            
            for c in range(COLS):

                if(isValid(r, c)):

                    board[r][c] = "Q"

                    rows.add(r)
                    cols.add(c)
                    leftDiagonal.add(r-c)
                    rightDiagonal.add(r+c)

                    function(r + 1)

                    rows.remove(r)
                    cols.remove(c)
                    leftDiagonal.remove(r-c)
                    rightDiagonal.remove(r+c)

                    board[r][c] = "."
        
        function(0)

        return res
