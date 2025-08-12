class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
        poss = []
        i = 1
        while i ** x <= n:
            poss.append(i)
            i += 1
        MOD = 10 ** 9 + 7
        # dp = [[-1] * (n + 1) for _ in range(len(poss))]
        # def dfs(i, s):
        #     if i >= len(poss):
        #         if s == n:
        #             return 1
        #         return 0
            
        #     if dp[i][s] != -1:
        #         return dp[i][s]
            
        #     pick = 0
        #     if s + (poss[i] ** x) <= n:
        #         pick = dfs(i + 1, s + (poss[i] ** x))
        #     nPick = dfs(i + 1, s)

        #     dp[i][s] = (pick + nPick) % MOD
        #     return dp[i][s]
        
        # return dfs(0, 0)

        dp = [[0] * (n + 1) for _ in range(len(poss) + 1)]

        dp[len(poss)][n] = 1
        

        for i in range(len(poss)-1, -1, -1):
            for s in range(n, -1, -1):
                
                pick = 0
                if s + (poss[i] ** x) <= n:
                    pick = dp[i + 1][s + (poss[i] ** x)]
                nPick = dp[i + 1][s]

                dp[i][s] = (pick + nPick) % MOD
        
        return dp[0][0] % MOD




        

