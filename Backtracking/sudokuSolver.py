class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = 9, 9
    
        # Initialize sets to track numbers in rows, columns, and squares
        rows = {i: set() for i in range(ROWS)}
        cols = {i: set() for i in range(COLS)}
        squares = {(r, c): set() for r in range(3) for c in range(3)}
        
        # Fill the sets with existing numbers on the board
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != ".":
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    squares[(r // 3, c // 3)].add(val)
        
        # Helper function to check if a value is valid in the current cell
        def isValid(row, col, val):
            return (
                val not in rows[row] and
                val not in cols[col] and
                val not in squares[(row // 3, col // 3)]
            )
        
        # Backtracking function
        def backtrack(r, c):
            if r == ROWS:  # Reached the end of the board
                return True
            if c == COLS:  # Move to the next row
                if(board[r][c - 1] not in rows[r]):
                    return False
                return backtrack(r + 1, 0)
            if board[r][c] != ".":  # Skip filled cells
                return backtrack(r, c + 1)
            
            for num in map(str, range(1, 10)):  # Try numbers 1 to 9
                if isValid(r, c, num):
                    # Place the number and update sets
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    squares[(r // 3, c // 3)].add(num)
                    
                    # Recurse to the next cell
                    if backtrack(r, c + 1):
                        return True
                    
                    # Backtrack: Remove the number
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    squares[(r // 3, c // 3)].remove(num)
            
            return False  # No valid number found for this cell
        
    # Start backtracking from the top-left corner
        backtrack(0, 0)
        
        return board




                


        
