class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # i is always increasing that implies that we can reach end row at the same time.
        rows = len(grid)
        cols = len(grid[0])

        memo = {}

        def function(r, c1, c2):
            if(r >= rows or c1 >= cols or c2 >= cols or c1 < 0 or c2 < 0):
                return float("-inf")
            if(r == rows -1):
                if(c1 != c2):
                    return grid[r][c1] + grid[r][c2]
                else:
                    return grid[r][c1]

            if((r, c1, c2) in memo):
                return memo[(r, c1, c2)]
            cherry = 0
            if(c1 == c2):
                cherry += grid[r][c1]
            else:
                cherry += grid[r][c1] + grid[r][c2]

            f1 = function(r + 1, c1, c2 + 1)
            f2 = function(r + 1, c1, c2 - 1)
            f3 = function(r + 1, c1, c2)
            f4 = function(r + 1, c1 + 1, c2)
            f5 = function(r + 1, c1 - 1, c2)
            f6 = function(r + 1, c1 + 1, c2 + 1)
            f7 = function(r + 1, c1 + 1, c2 - 1)
            f8 = function(r + 1, c1 - 1, c2 + 1)
            f9 = function(r + 1, c1 - 1, c2 - 1)

            cherry += max(f1, f2, f3, f4, f5, f6, f7, f8, f9)

            memo[(r, c1, c2)] = cherry
            return cherry

        return(function(0, 0, cols -1))

