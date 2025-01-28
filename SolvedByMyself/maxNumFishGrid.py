class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c, total):

            if(r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or grid[r][c] == 0):
                return
            
            total[0] += grid[r][c]
            visited.add((r, c))

            for dr, dc in directions:

                nr, nc = r + dr, c + dc

                dfs(nr, nc, total)
            
            return total

        res = 0
        for r in range(rows):
            for c in range(cols):
                if((r,c) not in visited and grid[r][c] > 0):
                    res = max(res, dfs(r, c, [0])[0])

        return(res)
