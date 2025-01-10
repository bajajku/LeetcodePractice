class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # find row

        l, r = 0, len(matrix)-1
        m = 0
        while l <= r:

            m = (l + r) // 2

            if(target < matrix[m][0]):
                r = m - 1
            
            elif(target > matrix[m][-1]):
                l = m + 1
            
            else:
                break
        
        l, r = 0, len(matrix[m]) - 1

        while l <= r:

            mid = (l + r) // 2

            if(target == matrix[m][mid]):
                return True
            
            elif(target < matrix[m][mid]):
                r = mid -1
            
            else:
                l = mid + 1
        
        return False
        
        
