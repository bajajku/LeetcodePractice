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

    # Bottom Up
    memo = [[0] * 2 for _ in range(len(prices) + 1)]
    
    for i in range(len(prices) - 1, -1, -1):

        for j in [0, 1]:
            res = 0
            if(j == 1):
                b = memo[i + 1][0] - prices[i]
                nB = memo[i + 1][1] + 0
                res =  max(b, nB)
            elif(j == 0):
                s = memo[i + 1][1] + prices[i]
                nS = memo[i + 1][0]
                res = max(s, nS)
            
            memo[i][j] = res
    
    return memo[0][1]



            
            

