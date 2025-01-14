class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ROWS, COLS = n, n

        totalElements = ROWS * COLS

        directions = {"right": (0, 1), "left": (0, -1), "top": (-1, 0), "bottom": (1, 0)}
        d = "right"

        r, c = 0, 0

        res = [[0] * COLS for _ in range(ROWS)]

        x = 0

        v = 1

        i = 0
        for i in range(1, totalElements +1):

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

            res[r][c] = i

            r += dire[0]
            c += dire[1]
            
        

        return res
            

# 2


# 1   2   3   4   5
# 16  17  18  19  6
# 15  24  25  20  7
# 14  23  22  21  8
# 13  12  11  10  9
