class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ROWS = len(board)
        COLS = len(board[0])

        rows = {i: set([]) for i in range(ROWS)}
        cols = {i: set([]) for i in range(COLS)}
        squares = {(r, c): set([]) for r in range(3) for c in range(3)} 

        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c] != "."):
                    if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3 )]:
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3,c//3)].add(board[r][c])


        return True
        
