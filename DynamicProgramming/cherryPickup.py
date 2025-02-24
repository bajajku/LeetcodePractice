class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        memo = {}
        def function(r1, c1, r2):
            c2 = r1 + c1 - r2
            if(r1 >= len(grid) or r2 >= len(grid) or c1 >= len(grid[0]) or c2 >= len(grid[0]) or grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float("-inf")
            if((r1, c1, r2) in memo):
                return memo[(r1, c1, r2)]

            if(r1 == len(grid) -1 and c1 == len(grid[0]) -1):
                return grid[r1][c1]
            cherry = 0
            if(r1 == r2 and c1 == c2):
                cherry += grid[r1][c1]

            else:
                cherry += grid[r1][c1] + grid[r2][c2]

            f1 = function(r1 + 1, c1, r2 + 1)
            f2 = function(r1 + 1, c1, r2)
            f3 = function(r1, c1 + 1, r2 + 1)
            f4 = function(r1, c1 + 1, r2)

            cherry += max(f1, f2, f3, f4)

            memo[(r1, c1, r2)] = cherry
            return cherry

        res = function(0, 0, 0)
        return res if res != float("-inf") else 0

        
        
