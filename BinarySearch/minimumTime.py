class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        l, r = 1, min(time) * totalTrips
        time.sort()

        def check(m):
            res = totalTrips
            for t in time:
                res -= (m // t)
            
            return res <= 0


        result = 0

        while l <= r:

            m = (l + r) // 2

            if(check(m)):
                result = m
                r = m - 1
            else:
                l = m + 1

        return(result)
        






