class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [(1, 0), (0, 1), (1, 1)]

        memo = [[0] * (cols+1) for _ in range(rows + 1)]
        maxVal = 0
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if(matrix[i][j] != "1"):
                    continue
                minVal = float("inf")
                for dr, dc in directions:
                    ni, nj = i + dr, j + dc
                    minVal = min(minVal, memo[ni][nj])
                
                memo[i][j] = minVal + 1
                maxVal = max(maxVal, minVal + 1)

        return maxVal ** 2


        # memo = {}
        # def function(i, j):

        #     if(i == rows or j == cols or matrix[i][j] == "0"):
        #         return 0
            
        #     if((i, j) in memo):
        #         return memo[(i,j)]

        #     minVal = float("inf")
        #     for dr, dc in directions:
        #         ni, nj = i + dr, j + dc
        #         minVal = min(minVal, function(ni, nj))
            
        #     memo[(i, j)] = minVal + 1
        #     return minVal + 1

        # maxVal = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         if(matrix[r][c] != "0"):
        #             maxVal = max(maxVal, function(r, c))
        
        # return maxVal ** 2




            
