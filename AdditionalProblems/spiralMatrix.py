class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        ROWS, COLS = len(matrix), len(matrix[0])

        totalElements = ROWS * COLS

        directions = {"right": (0, 1), "left": (0, -1), "top": (-1, 0), "bottom": (1, 0)}
        d = "right"

        r, c = 0, 0

        res = []

        x = 0

        v = 1

        i = 0
        for _ in range(totalElements):

            if(v == 4):
                x += 1
                v = 0

            if(c == COLS - x - 1 and d == "right"):
                d = "bottom"
                v += 1
            elif(r == ROWS - x -1 and d == "bottom"):
                d = "left"
                v += 1
            
            elif(c == x and d == "left"):
                d = "top"
                v += 1
            elif(r == x and d == "top"):
                d = "right"
                v += 1
            
            

            dire = directions[d]

            res.append(matrix[r][c])

            r += dire[0]
            c += dire[1]
            
        

        return res
        






        
