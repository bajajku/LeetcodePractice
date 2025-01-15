class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        ROWS = len(mat)
        COLS = len(mat[0])

        if(ROWS * COLS != r * c):
            return mat
        
        flatten = []
        res = [[0]*c for _ in range(r)]
        for i in range(ROWS):
            for j in range(COLS):

                flatten.append(mat[i][j])
        
        k = 0
        for i in range(len(res)):
            for j in range(len(res[0])):

                res[i][j] = flatten[k]
                k += 1
        
        return
