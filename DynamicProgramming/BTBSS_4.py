class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        #Top DOWNNNN
        memo = [[[-1] * (k + 1) for _ in range(2)] for _ in range(len(prices))]
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
        
        return (function(0, 1, k))

        # Bottom Up:

        numTransac = k
        memo = [[[0] * (k + 1) for _ in range(2)] for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):

            for j in [0, 1]:

                for k in range(1, numTransac + 1):
                    res = 0
                    if(j == 1):
                        b = memo[i + 1][0][k] - prices[i]
                        nB = memo[i + 1][1][k] + 0
                        res =  max(b, nB)
                    elif(j == 0):
                        s = memo[i + 1][1][k-1] + prices[i]
                        nS = memo[i + 1][0][k]
                        res = max(s, nS)
                    
                    memo[i][j][k] = res
        
        return memo[0][1][k]
