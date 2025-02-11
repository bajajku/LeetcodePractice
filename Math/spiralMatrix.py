class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        v = 1
        directions = {"top": (-1, 0), "bot": (1, 0), "right": (0, 1), "left": (0, -1)}
        d = "right"

        r, c = 0, 0
        x = 0

        res = [] 

        while i != rows * cols:

            if v == 4:
                x += 1
                v = 0

            if(d == "right" and c == cols - x - 1):
                d = "bot"
                v += 1
            elif(d == "bot" and r == rows - x - 1):
                d = "left"
                v += 1
            elif(d == "left" and c == x):
                d = "top"
                v += 1
            elif(d == "top" and r == x):
                d = "right"
                v += 1
            
            
            res.append(matrix[r][c])

            r, c = r + directions[d][0], c + directions[d][1]
            i += 1

        return(res)
            




