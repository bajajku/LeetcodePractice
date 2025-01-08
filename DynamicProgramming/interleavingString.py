class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        if(len(s1) + len(s2) != len(s3)):
            return False

        memo = {}
        def function(i, j):

            if(i < 0 and j < 0):
                return True
            if i < 0:
                if(s2[:j + 1] == s3[:j + 1]):
                    return True
                else:
                    return False
            
            if((i,j) in memo):
                return memo[(i,j)]
            
            if(j < 0):
                if(s1[:i + 1] == s3[:i + 1]):
                    return True
                else:
                    return False

            pickI = False
            pickJ = False
            if(s1[i] == s3[i + j + 1]):
                pickI = function(i-1, j)
            
            if(s2[j] == s3[i+j + 1]):
                pickJ = function(i, j-1)

            memo[(i,j)] = pickI or pickJ

            return memo[(i,j)]
        
        return function(len(s1) -1, len(s2) -1)
