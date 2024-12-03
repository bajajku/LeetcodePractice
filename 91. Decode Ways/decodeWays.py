'''
Initial intuition:
Recursive case: we have to index track, if we reach end index its a valid decode,
and we can increase the result by 1

So in general a number can be:
1 digit or (2 digit and <= 26, and no leading 0) to be valid.

Intuition was decent, but wasn't able to code it. :(

'''



def numDecodings(s: str) -> int:

    '''  
    Top-Down: 
    Our base case will be len(s), we assume that a full string will produce 1 decode way if there is no 0 in it
    We can memoize repetitive steps, It should look like this:
    If we encounter any 0 we will return 0, if index already present in memo, return memo[i]
    S, it goes recursively for [3, 13, 213, 1213] and in the end we have memo[0] as result (if present),
    which we are directly returning.

    "1213" 
    dry run:
    dfs(0): dfs(0 + 1) + dfs(0 + 2)
    dfs(1): dfs(1 + 1) + dfs(1 + 2)
    dfs(2): dfs(2 + 1) + dfs(2 + 2)
    '''
    memo = {len(s): 1}

    def dfs(i):

        if i in memo:
            return memo[i]

        if s[i] == "0":
            return 0
        
        res = dfs(i + 1)

        if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
            res += dfs(i+2)
        
        memo[i] = res
        return res

        
    return dfs(0)

    # Bottom up
    def numDecodings(s: str) -> int:

        dp = {len(s): 1}
        '''Iterating backwards like "1213":
        [3, 13, 213, 1213]
        
        UPDATING if digit is 0, we as telling that starting from this index,
        result is 0, 

        I just realized 2 0's together will always decode 0
        '''
        for i in range(len(s) -1, -1, -1):
            if(s[i] == "0"):
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if (i + 1 < len(s)) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]
            
        print(dp)
        return dp[0]
            

            
            

        