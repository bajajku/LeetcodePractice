class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if(len(prices) == 0):
            return 0

        minPrice = prices[0]

        res = 0

        for p in prices:

            if p < minPrice:
                minPrice = p
            
            res = max(res, p - minPrice)
        
        return res
