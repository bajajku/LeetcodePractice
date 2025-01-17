
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        ROWS = len(heights)
        COLS = len(heights[0])

        pac_set = set()
        atl_set = set()
        def dfs(r, c, ocean_set, prev):

            if(r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in ocean_set or heights[r][c] < prev):
                return
            
            ocean_set.add((r, c))

            newPrev = heights[r][c]
            dfs(r + 1, c, ocean_set, newPrev)
            dfs(r - 1, c, ocean_set, newPrev)
            dfs(r, c + 1, ocean_set, newPrev)
            dfs(r, c - 1, ocean_set, newPrev)


            return
        
        for r in range(ROWS):
            dfs(r, 0, pac_set, float("-inf"))
            dfs(r, COLS - 1, atl_set, float("-inf"))

        for c in range(COLS):
            dfs(0, c, pac_set, float("-inf"))
            dfs(ROWS - 1, c, atl_set, float("-inf"))

        res = []
        
        for i in pac_set:
            if(i in atl_set):
                res.append([i[0], i[1]])

        return res
