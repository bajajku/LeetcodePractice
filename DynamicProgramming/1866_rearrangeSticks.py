class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [[-1] * (k+1) for _ in range(n + 1)]
        def function(n, k):

            if n == k == 0:
                return 1
            
            if dp[n][k] != -1:
                return dp[n][k]
            
            if n == 0 and k > 0 or n > 0 and k == 0:
                return 0
            
            pickTall = function(n - 1, k - 1)
            nPickTall = function(n - 1, k) * (n - 1)

            dp[n][k] = (pickTall + nPickTall) % MOD
            return dp[n][k]
        
        return function(n, k)

                    
