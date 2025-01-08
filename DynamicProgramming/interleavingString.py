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

        '''
        Tabulation :
        '''
        # Check if the lengths match
        # if len(s1) + len(s2) != len(s3):
        #     return False

        # n, m = len(s1), len(s2)

        # # Create a DP table initialized with False
        # dp = [[False] * (m + 1) for _ in range(n + 1)]

        # # Base case: both strings are empty
        # dp[0][0] = True

        # # Fill the first row (when s1 is empty)
        # for j in range(1, m + 1):
        #     if dp[0][j - 1] and s2[j - 1] == s3[j - 1]:
        #         dp[0][j] = True
        #     else:
        #         dp[0][j] = False

        # # Fill the first column (when s2 is empty)
        # for i in range(1, n + 1):
        #     if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
        #         dp[i][0] = True
        #     else:
        #         dp[i][0] = False

        # # Fill the rest of the table
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         pickI = False
        #         pickJ = False

        #         # Check if the current character of s1 matches s3
        #         if dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
        #             pickI = True

        #         # Check if the current character of s2 matches s3
        #         if dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
        #             pickJ = True

        #         # Assign the result based on either condition being true
        #         if pickI or pickJ:
        #             dp[i][j] = True
        #         else:
        #             dp[i][j] = False

        # # The final result is in the bottom-right corner
        # return dp[n][m]
