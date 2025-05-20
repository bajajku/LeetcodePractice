class Solution:
    '''
    00  01  02  03
    10  11  12  13
    20  21  22  23
    30  31  32  33
    
    
    '''

    def __init__(self):
        self.cols = set()
        self.left_diagonal = set()
        self.right_diagonal = set()
        self.result = []
    
    def buildState(self, n):
        state = [["."] * n for _ in range(n)]
        return state
        
    def isValid(self, row, col):
        if col not in self.cols and (row + col) not in self.left_diagonal and (col - row) not in self.right_diagonal:
            return True
        return False


    def update(self, row, col, command):
        if command == "insert":
            self.cols.add(col)
            self.left_diagonal.add(row + col)
            self.right_diagonal.add(col - row)
        elif command == "delete":
            self.cols.remove(col)
            self.left_diagonal.remove(row + col)
            self.right_diagonal.remove(col - row)
    
    def backtrack(self, r, state, n):
        if r == n:
            self.result.append(["".join(row) for row in state])  # deep copy in string format
            return
        
        for c in range(n):
            if self.isValid(r, c):
                state[r][c] = "Q"
                self.update(r, c, "insert")

                self.backtrack(r + 1, state, n)

                state[r][c] = "."
                self.update(r, c, "delete")
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        state = self.buildState(n)
        self.backtrack(0, state, n)
        return(self.result)
        
