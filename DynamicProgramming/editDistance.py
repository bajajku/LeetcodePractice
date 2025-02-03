class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)

        memo = [[-1] * n for _ in range(m)]

        def function(i, j):

            if(i == m):
                return n - j
            if(j == n):
                return m - i
            
            if(memo[i][j] != -1):
                return memo[i][j]

            if(word1[i] == word2[j]):
                memo[i][j] = function(i + 1, j + 1)
                return function(i + 1, j + 1)
            else:
                remI = 1 + function(i + 1, j)
                replI = 1 + function(i, j + 1)
                insI = 1 + function(i + 1, j + 1)
                
                memo[i][j] = min(remI, replI, insI)
                return min(remI, replI, insI)

        return(function(0, 0))
                

