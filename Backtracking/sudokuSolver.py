class Solution:

    def __init__(self):
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.sub_boxes = [set() for _ in range(9)]
    
    def initialState(self, board):
        for r in range(len(board)):
            for c in range(len(board[0])):
                ele = board[r][c]
                if ele != ".":
                    self.rows[r].add(ele)
                    self.cols[c].add(ele)
                    self.sub_boxes[(r // 3) * 3 + (c // 3)].add(ele)
        
    def isValid(self, num, r, c):
        if num not in self.rows[r] and num not in self.cols[c] and num not in self.sub_boxes[(r // 3) * 3 + (c // 3)]:
            return True
        return False

    def update(self, num, r, c, command):
        if command == "insert":
            self.rows[r].add(num)
            self.cols[c].add(num)
            self.sub_boxes[(r // 3) * 3 + (c // 3)].add(num)
        
        elif command == "delete":
            self.rows[r].remove(num)
            self.cols[c].remove(num)
            self.sub_boxes[(r // 3) * 3 + (c // 3)].remove(num)

    def backtrack(self, r, c, board):

        if r == 9:
            return True
        
        if c == 9:
            return self.backtrack(r + 1, 0, board)
        
        if board[r][c] != ".":
            return self.backtrack(r, c + 1, board)
        
        for num in range(1, 10):
            num = str(num)

            if self.isValid(num, r, c):

                board[r][c] = num
                self.update(num, r, c, "insert")
                
                if self.backtrack(r, c + 1, board):
                    return True
                
                self.update(num, r, c, "delete")
                board[r][c] = "."

    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.initialState(board)

        self.backtrack(0, 0, board)

