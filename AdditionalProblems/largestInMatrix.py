class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        res = [[0] * (n-2) for _ in range(n-2)]


        for ri in range(n-2):
            for ci in range(n-2):

                maxi = float("-inf")
                for r in range(3):
                    for c in range(3):
                        maxi = max(maxi, grid[r + ri][c + ci])
                
                res[ri][ci] = maxi


        
        return res




        
        
