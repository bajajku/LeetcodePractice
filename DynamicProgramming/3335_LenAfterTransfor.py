class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
        # MOD = 10**9 + 7

        # memo = [[-1] * (t + 1) for _ in range(26)]

        # def function(char, t):

        #     ordChar = ord(char) - ord('a')
        #     if memo[ordChar][t] != -1:
        #         return memo[ordChar][t]
        #     if t == 0:
        #         return 1
            
        #     res = 0
        #     if char == 'z':
        #         res += (function('a', t - 1) + function('b', t - 1)) % MOD
        #     else:
        #         nextChar = chr(ord(char) + 1)
        #         res += function(nextChar, t - 1) % MOD
        #     memo[ordChar][t] = res % MOD
        #     return memo[ordChar][t]

        # result = 0
        # for c in s:
        #     result += function(c, t) % MOD

        # return(result) % MOD

        MOD = 10**9 + 7
        # This maps each character to (0 - 25), i.e their relative index (0- based)
        charToInd = {i: ord(i) - ord('a') for i in 'abcdefghijklmnopqrstuvwxyz'}

        print(charToInd)
        memo = {}
        def function(c):

            if c < 26:
                return 1
            
            if c in memo:
                return memo[c]
            
            count = function(c - 26) + function(c - 25)

            memo[c] = count
            return count
        
        ans = 0
        for char in s:
            ans += function(charToInd[char] + t) % MOD
        return ans % MOD





        






