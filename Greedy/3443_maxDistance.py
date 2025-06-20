class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        global count
        count = Counter(s)

        '''
        NW - 2

        NE - 2

        SW - 2

        SE - 2
        
        '''

        def f(A, B, nA, nB, k):
            maxVal = float("-inf")
            t = 0
            for c in s:

                if c == A or c == B:
                    t += 1
                
                else:
                    if k:
                        k -= 1
                        t += 1
                    else:
                        t -= 1
                maxVal = max(maxVal, t)
            
            return maxVal


        return max(f('N', 'W', 'S', 'E', k), f('N', 'E', 'S', 'W', k), f('S', 'W', 'N', 'E', k), f('S', 'E', 'N', 'W', k))         
