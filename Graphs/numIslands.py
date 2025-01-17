'''
Observation:

Keep track of visited in a set as well so we dont have to visit the same index twice.
1) It is an seperate island if it is 1 and all of its valid sides are 0
    -> count += 1
    -> mark [r][c] as visited
2) It is the same island if it's 1 and atleast one of it's neighbour is 1:
    -> count remains same.
    -> mark [r][c] as visited
3) For each cell we will run the CheckIsland() if it's not in visited and not equal to 0 else we skip.


What I did wrong:
1) Coding was in awrong direction
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        def dfs(r, c):

            if(r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == "0"):
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            dfs(r - 1, c)

            return
            
            

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == "1" and (r, c) not in visited):
                    res += 1
                    dfs(r, c)
        
        return(res)



            




        
