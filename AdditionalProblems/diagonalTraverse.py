class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

        '''
        property of right diagonal's sum(r+c) are equal.

        also

        Main Intuition: start with up rightDiagonal then switch, until all elements are traversed
        
        00 01 02 00

        10 11 12 00

        20 21 22 00
        
        00 00 00 00

        [00, 01, 10, 20, 11, 02, 12, 21, 22]

        '''

        

        ROWS = len(mat)
        COLS = len(mat[0])

        r, c = 0, 0
        res = []
        d = 1  # 1 for up, 0 for down

        while len(res) < ROWS * COLS:
            res.append(mat[r][c])

            if d == 1:  # Moving up
                if c == COLS - 1:  # Hit the right boundary
                    d = 0
                    r += 1
                elif r == 0:  # Hit the top boundary
                    d = 0
                    c += 1
                else:  # Regular upward move
                    r -= 1
                    c += 1

            elif d == 0:  # Moving down
                if r == ROWS - 1:  # Hit the bottom boundary
                    d = 1
                    c += 1
                elif c == 0:  # Hit the left boundary
                    d = 1
                    r += 1
                else:  # Regular downward move
                    r += 1
                    c -= 1

        return res










