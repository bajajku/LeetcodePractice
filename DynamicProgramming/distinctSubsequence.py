class Solution:

    def numDistinct(self, s: str, t: str) -> int:

        '''
        so this function checks:
        
            f(i, j) signifies check occurences of [0...j] in string [0...i]
        
         '''

         '''
         we only increment j if s[i] == s[j]

         and i will always be incremented no matter what,
         
         '''
        if(len(t) > len(s)):
            return 0
        
        # memo = [[-1] * len(t) for _ in range(len(s))]
        # def function(i, j):

        #     if(j == len(t)):
        #         return 1
        #     if(i == len(s)):
        #         return 0
        #     if(memo[i][j] != -1):
        #         return memo[i][j]

        #     res = 0
        #     if(s[i] == t[j]):
        #         res = function(i +1, j + 1) + function(i + 1, j)
        #     else:
        #         res = function(i + 1, j)
        #     memo[i][j] = res
        #     return res

        # return function(0, 0)

        memo = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s) + 1):
            memo[i][-1] = 1
        
        
        for i in range(len(s)- 1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                res = 0
                if(s[i] == t[j]):
                    res = memo[i + 1][j + 1] + memo[i + 1][j]
                else:
                    res = memo[i+1][j]
                memo[i][j] = res
        
        return memo[0][0]





            
