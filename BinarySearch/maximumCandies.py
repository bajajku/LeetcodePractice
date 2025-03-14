class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        def calculate(x, k):

            for n in candies:

                y = n // x
                k -= y
                if(k <= 0):
                    return True
            
            return False
        
        l, r = 1, max(candies)
        res = 0

        while l <= r:

            m = (l+r) // 2

            if(calculate(m, k)):
                res = m
                l = m + 1
            else:
                r = m - 1


        return res



