class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        l, r = 1, max(piles)

        res = max(piles)
        while l <= r:

            m = (l + r) // 2

            hour = 0

            for p in piles:
                
                hour += math.ceil(float(p) / m)
            
            if(hour <= h):
                res = m
                r = m - 1
            
            elif(hour > h):
                l = m + 1
        
        return(res)
        





        
