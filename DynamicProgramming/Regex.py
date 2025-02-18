class Solution:

    '''
    conditions:

        -> if char + * then we can have 0 or more chars
        -> if i == j then move next step
        -> 
    '''
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}
        def function(i, j):
            # Handle base cases
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            
            if((i, j) in memo):
                return memo[(i,j)]

            res = False

            if j + 1 < len(p) and p[j + 1] == '*':
                # Handle wildcard matching
                if i < len(s) and (s[i] == p[j] or p[j] == "."):
                    res = function(i + 1, j) or function(i, j + 2)
                else:
                    res = function(i, j + 2)
            else:
                if i < len(s) and (p[j] == '.' or s[i] == p[j]):
                    res = function(i + 1, j + 1)
            memo[(i, j)] = res
            return res
        
        return(function(0, 0))

        memo = [[False] * (len(p)+1) for _ in range(len(s)+ 1)]

        memo[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):

                res = False
                if(j + 1 < len(p) and p[j + 1] == "*"):
                    if i < len(s) and (s[i] == p[j] or p[j] == "."):
                        res = memo[i+1][j] or memo[i][j+2]
                    else:
                        res = memo[i][j+2]
                elif i < len(s) and (s[i] == p[j] or p[j] == "."):
                    res = memo[i + 1][j + 1]
                memo[i][j] = res
        
        return(memo[0][0])
