class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """

        rows = len(mat)
        cols = len(mat[0])
        
        hm = {}

        rowFreq = [0] * rows
        colFreq = [0] * cols


        for r in range(rows):
            for c in range(cols):
                hm[mat[r][c]] = [r, c]


        
        for i in range(len(arr)):
            
            r, c = hm[arr[i]]

            rowFreq[r] += 1
            colFreq[c] += 1

            if(rowFreq[r] == cols or colFreq[c] == rows):
                return i
        
        return -1





        
