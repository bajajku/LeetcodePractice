class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        freshOranges = 0

        rotten_oranges = deque()
        for r in range(ROWS):
            for c in range(COLS):

                if(grid[r][c] == 2):
                    rotten_oranges.append((r, c))
                    visited.add((r, c))
                elif(grid[r][c] == 1):
                    freshOranges += 1

        res = 0
        def isValid(r, c):
            if(r < 0 or c < 0 or (r, c) in visited or r == ROWS or c == COLS or grid[r][c] == 0):
                return False
            
            return True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while rotten_oranges and freshOranges > 0:

            for i in range(len(rotten_oranges)):

                r, c = rotten_oranges.popleft()

                for row, col in directions:
                    nr = r + row
                    nc = c + col

                    if(isValid(nr, nc)):
                        rotten_oranges.append((nr, nc))
                        visited.add((nr, nc))
                        freshOranges -= 1
            
            res += 1
        
        return res if(freshOranges == 0) else -1
                
                


        

        
