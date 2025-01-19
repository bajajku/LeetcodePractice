class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Top DOWNNNN
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(len(prices))]
        def function(i, buy, k):
            res = 0
            if(i == len(prices)):
                return 0
            
            if(k == 0):
                return 0

            if(memo[i][buy][k] != -1):
                return memo[i][buy][k]

            if(buy == 1):
                b = function(i + 1, 0, k) - prices[i]
                nB = function(i+1, 1, k)
                res = max(b, nB)
            elif(buy == 0):
                s = function(i + 1, 1, k - 1) + prices[i]
                nS = function(i+1, 0, k)
                res = max(s, nS)
            
            memo[i][buy][k] = res

            return res
        
        return (function(0, 1, 2))
