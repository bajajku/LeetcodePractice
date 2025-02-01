class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # main intuition is from all 0 find the maximum island you can form

        rows = len(grid)
        cols = len(grid[0])

        zero_cells = set()
        visited = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]


        hm = {} # {i_id: len(island) }
        hm2 = {} # {cells : id}
        # we need something with unique islands with its length and cell's inside that island

        def dfs(r, c):

            if(r < 0 or c < 0 or r == rows or c == rows or (r, c) in visited or grid[r][c] == 0):
                return
            
            visited.add((r, c))
            temp.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        island_id = 0
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 0):
                    zero_cells.add((r, c))
                elif((r, c) not in visited and grid[r][c] == 1):

                    temp = set()
                    dfs(r, c)
                    hm[island_id] = len(temp)
                    for i, j in temp:
                        hm2[(i, j)] = island_id

                    island_id += 1
        
        if(len(zero_cells) == 0):
            return rows * cols
        elif(len(zero_cells) == rows * cols):
            return 1
        

        else:
            res = float("-inf")
            for r, c in zero_cells:
                neigh = set()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if(nr < 0 or nc < 0 or nr == rows or nc == rows or grid[nr][nc] == 0):
                        continue
                    neigh.add(hm2[nr, nc])
                tempRes = 1
                for i in neigh:
                    tempRes += hm[i]
                res = max(res, tempRes)



        return(res)
            


