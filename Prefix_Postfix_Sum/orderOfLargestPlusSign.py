class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        
        
        mat = [[1] * n for _ in range(n)]

        for r, c in mines:
            mat[r][c] = 0
        
        
        left = [[0] * n for i in range(n)]
        top = [[0] * n for i in range(n)]
        right = [[0] * n for i in range(n)]
        bottom = [[0] * n for i in range(n)]
        
        
        for i in range(n):
            for j in range(n):

                if(mat[i][j] != 0):
                    left[i][j] = 1 + left[i][j-1] if j > 0 else 1
                    top[i][j] = 1 + top[i-1][j] if i > 0 else 1
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):

                if(mat[i][j] != 0):
                    right[i][j] = 1 + right[i][j+1] if j < n-1 else 1
                    bottom[i][j] = 1 + bottom[i+1][j] if i < n -1 else 1
        
        res = 0

        for i in range(n):
            for j in range(n):

                if(mat[i][j] != 0):
                    order = min(left[i][j], right[i][j], top[i][j], bottom[i][j])
                    res = max(res, order)

        return res



        
