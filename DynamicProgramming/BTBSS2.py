class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        memo = [[-1] * 2 for _ in range(len(prices))]
        def function(i, buy):
            res = 0
            if(i == len(prices)):
                return res

            if(memo[i][buy] != -1):
                return memo[i][buy]

            if(buy == 1):
                b = function(i + 1, 0) - prices[i]
                nB = function(i+1, 1)
                res = max(b, nB)
            elif(buy == 0):
                s = function(i + 1, 1) + prices[i]
                nS = function(i+1, 0)
                res = max(s, nS)
            
            memo[i][buy] = res

            return res
        
        return (function(0, 1))



            
            

