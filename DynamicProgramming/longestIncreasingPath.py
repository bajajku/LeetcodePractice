class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        memo = {}

        def function(cur, prevVal):
            r, c = cur
            if(r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal):
                return 0

            if((r, c) in memo):
                return memo[(r,c)]
            res = 1
            left = 1 + function((r + 1, c), matrix[r][c])
            right = 1 + function((r - 1, c), matrix[r][c])
            top = 1 + function((r, c + 1), matrix[r][c])
            bot = 1 + function((r, c - 1), matrix[r][c])

            memo[(r,c)] = max(left, right, top, bot, res)
            return max(left, right, top, bot, res)

        result = float("-inf")
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                result = max(result, function((r,c), -1))
        
        return(result)
        
